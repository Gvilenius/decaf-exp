package decaf.frontend.typecheck;

import decaf.driver.Config;
import decaf.driver.Phase;
import decaf.driver.error.*;
import decaf.frontend.scope.LambdaScope;
import decaf.frontend.scope.LocalScope;
import decaf.frontend.scope.ScopeStack;
import decaf.frontend.symbol.*;
import decaf.frontend.tree.Pos;
import decaf.frontend.tree.Tree;
import decaf.frontend.type.*;
import decaf.lowlevel.log.IndentPrinter;
import decaf.printing.PrettyScope;

import javax.lang.model.type.ErrorType;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Stack;

/**
 * The typer phase: type check abstract syntax tree and annotate nodes with inferred (and checked) types.
 */
public class Typer extends Phase<Tree.TopLevel, Tree.TopLevel> implements TypeLitVisited {

    private Stack<String> stk = new Stack<>();
    public Typer(Config config) {
        super("typer", config);
    }

    @Override
    public Tree.TopLevel transform(Tree.TopLevel tree) {
        var ctx = new ScopeStack(tree.globalScope);
        tree.accept(this, ctx);
        return tree;
    }

    @Override
    public void onSucceed(Tree.TopLevel tree) {
        if (config.target.equals(Config.Target.PA2)) {
            var printer = new PrettyScope(new IndentPrinter(config.output));
            printer.pretty(tree.globalScope);
            printer.flush();
        }
    }

    @Override
    public void visitTopLevel(Tree.TopLevel program, ScopeStack ctx) {
        for (var clazz : program.classes) {
            clazz.accept(this, ctx);
        }
    }

    @Override
    public void visitClassDef(Tree.ClassDef clazz, ScopeStack ctx) {
        ctx.open(clazz.symbol.scope);
        for (var field : clazz.fields) {
            field.accept(this, ctx);
        }
        ctx.close();
    }

    @Override
    public void visitMethodDef(Tree.MethodDef method, ScopeStack ctx) {
        ctx.open(method.symbol.scope);
        if (!method.body.isEmpty()) {
            method.body.get().accept(this, ctx);
            if (!method.symbol.type.returnType.isVoidType() && !method.body.get().returns) {
                issue(new MissingReturnError(method.body.get().pos));
            }
        }
        ctx.close();
    }

    /**
     * To determine if a break statement is legal or not, we need to know if we are inside a loop, i.e.
     * loopLevel {@literal >} 1?
     * <p>
     * Increase this counter when entering a loop, and decrease it when leaving a loop.
     */
    private int loopLevel = 0;

    @Override
    public void visitBlock(Tree.Block block, ScopeStack ctx) {
        ctx.open(block.scope);
        block.type = BuiltInType.VOID;
        for (var stmt : block.stmts) {

            stmt.accept(this, ctx);
            if (!stmt.returnTypes.isEmpty()) {
                block.returnTypes.addAll(stmt.returnTypes);
            }
        }
        ctx.close();
        block.returns = !block.stmts.isEmpty() && block.stmts.get(block.stmts.size() - 1).returns;
    }
    public Type typeBound(List<Type> typeList, Pos pos, Boolean isUpper){
        int k = 0;
        var t1 = typeList.get(k);
        while (t1.eq(BuiltInType.NULL)){
            t1 = typeList.get(k++);
            if (k == typeList.size()) return t1;
        }

        if (t1.isBaseType() || t1.isVoidType() || t1.isArrayType()) {
            for (var t2 : typeList ) {
                if (!t2.eq(t1)) {
                        issue(new IncompatReturnTypesError(pos));
                        return null;
                    }
            }
                return t1;
        }
        else if (t1.isFuncType()){
            ArrayList<ArrayList<Type>> paramList = new ArrayList<>();
            ArrayList<Type> returnList = new ArrayList<>();
            returnList.add(((FunType)t1).returnType);

            for (int i = 0; i < ((FunType)t1).arity(); ++i){
                paramList.add(new ArrayList<Type>());
                paramList.get(i).add(((FunType) t1).argTypes.get(i));
            }

            for (var t2 : typeList ) {
                if (t2.isFuncType() && ((FunType) t2).arity() == ((FunType) t1).arity()) {
                    returnList.add(((FunType) t2).returnType);
                    for (int i = 0; i < ((FunType) t1).arity(); ++i) {
                        paramList.get(i).add(((FunType) t2).argTypes.get(i));
                    }
                } else {
                    issue(new IncompatReturnTypesError(pos));
                    return null;
                }
            }
            ArrayList<Type> paramLowerBoundList = new ArrayList<>();
            for (var paramArray: paramList){
                var paramLowerBound = typeBound(paramArray, pos, !isUpper);

                if (paramLowerBound == null) {
                    return null;
                }
                paramLowerBoundList.add(paramLowerBound);

            }

            Type returnType = typeBound(returnList, pos, isUpper);

            if (returnType == null) {
                return null;
            }
            return new FunType(returnType, paramLowerBoundList);
        }
        else if (t1.isClassType()){
            //TODO
            ClassType p = (ClassType) t1;
            if (isUpper) {
                for (var t2 : typeList ) {
                    while (!(t2.subtypeOf(p))) {
                        if (p.superType.isPresent())
                            p = p.superType.get();
                        else {
                            issue(new IncompatReturnTypesError(pos));
                            return null;
                        }
                    }
                }
                return p;
            }
            else{
                //TODO
                for (var t2 : typeList ) {
                    if (p.subtypeOf(t2)) continue;
                    else if (t2.subtypeOf(p)) p = (ClassType) t2;
                    else{
                        issue(new IncompatReturnTypesError(pos));
                        return null;
                    }
                }
                return p;
            }
        }
        return null;
    }


    @Override
    public void visitAssign(Tree.Assign stmt, ScopeStack ctx) {
        stmt.lhs.accept(this, ctx);
        stmt.rhs.accept(this, ctx);
        var lt = stmt.lhs.type;
        var rt = stmt.rhs.type;
        if (lt.noError()){
            if(!rt.subtypeOf(lt))
                issue(new IncompatBinOpError(stmt.pos, lt.toString(), "=", rt.toString()));

            if (stmt.lhs instanceof Tree.VarSel){
                var lhs = (Tree.VarSel) stmt.lhs;
                if (lhs.receiver.isPresent()
                        && lhs.receiver.get().type!= null
                        && lhs.receiver.get().type.isClassType()
                        &&!(lhs.receiver.get() instanceof Tree.This)){
                    //类名只能调静态方法，出现就是报错，非静态方法在VarSel节点就已经报错
                    //过滤this.变量

                    var clazz = ctx.getClass(((ClassType)lhs.receiver.get().type).name);
                    if (clazz.scope.get(lhs.name) instanceof MethodSymbol)
                        issue(new AssignMethodMemberError(stmt.pos, lhs.name));
                }
                else if (ctx.currentClass().scope.get(lhs.name) instanceof MethodSymbol){
                    //本类成员变量可以赋值，方法不行
                    issue(new AssignMethodMemberError(stmt.pos, lhs.name));
                }
            }

            if(stmt.lhs instanceof Tree.VarSel //非数组,IndexSel
                    && ctx.currentScope() instanceof LocalScope
                    && ctx.currentLambda() != null //在lambda作用
                    && !((LocalScope)ctx.currentScope()).have(((Tree.VarSel)stmt.lhs).name) //不在当前lambda作用域
                    &&((Tree.VarSel)stmt.lhs).receiver.isEmpty()){ //非成员变量的引用
                    issue(new LambdaAssignVarOutOfScopeError(stmt.pos));
            }
        }
    }

    @Override
    public void visitExprEval(Tree.ExprEval stmt, ScopeStack ctx) {
        stmt.expr.accept(this, ctx);
    }


    @Override
    public void visitIf(Tree.If stmt, ScopeStack ctx) {
        checkTestExpr(stmt.cond, ctx);
        stmt.trueBranch.accept(this, ctx);
        stmt.falseBranch.ifPresent(b -> b.accept(this, ctx));
        // if-stmt returns a value iff both branches return
        stmt.returnTypes.addAll(stmt.trueBranch.returnTypes);
        if (stmt.falseBranch.isPresent()) stmt.returnTypes.addAll(stmt.falseBranch.get().returnTypes);
        stmt.returns = stmt.trueBranch.returns && stmt.falseBranch.isPresent() && stmt.falseBranch.get().returns;
    }

    @Override
    public void visitWhile(Tree.While loop, ScopeStack ctx) {
        checkTestExpr(loop.cond, ctx);
        loopLevel++;
        loop.body.accept(this, ctx);
        loop.returns = loop.body.returns;
        loopLevel--;
        loop.returnTypes = loop.body.returnTypes;
    }

    @Override
    public void visitFor(Tree.For loop, ScopeStack ctx) {
        ctx.open(loop.scope);
        loop.init.accept(this, ctx);
        checkTestExpr(loop.cond, ctx);
        loop.update.accept(this, ctx);
        loopLevel++;
        for (var stmt : loop.body.stmts) {
            stmt.accept(this, ctx);
            loop.returnTypes.addAll(stmt.returnTypes);
            if (stmt.returns) loop.returns= true;
        }
        loopLevel--;
        ctx.close();

    }

    @Override
    public void visitBreak(Tree.Break stmt, ScopeStack ctx) {
        if (loopLevel == 0) {
            issue(new BreakOutOfLoopError(stmt.pos));
        }
    }

    //TODO
    @Override
    public void visitReturn(Tree.Return stmt, ScopeStack ctx) {
        if (ctx.currentLambda() != null){
            stmt.expr.ifPresent(e -> e.accept(this, ctx));
            stmt.returns = true;
            stmt.returnTypes.add(stmt.expr.isPresent() ?(stmt.expr.get().type == null?BuiltInType.NULL : stmt.expr.get().type): BuiltInType.VOID);
            return;
        }
        var expected = ctx.currentMethod().type.returnType;
        stmt.expr.ifPresent(e -> e.accept(this, ctx));
        var actual = stmt.expr.map(e -> e.type).orElse(BuiltInType.VOID);
        if (actual.noError() && !actual.subtypeOf(expected)) {
            issue(new BadReturnTypeError(stmt.pos, expected.toString(), actual.toString()));
        }
        stmt.returns = stmt.expr.isPresent();
        stmt.returnTypes.add(stmt.expr.isPresent() ?stmt.expr.get().type: BuiltInType.VOID);
    }

    @Override
    public void visitPrint(Tree.Print stmt, ScopeStack ctx) {
        int i = 0;
        for (var expr : stmt.exprs) {
            expr.accept(this, ctx);
            i++;
            if (expr.type.noError() && !expr.type.isBaseType()) {
                issue(new BadPrintArgError(expr.pos, Integer.toString(i), expr.type.toString()));
            }
        }
    }

    private void checkTestExpr(Tree.Expr expr, ScopeStack ctx) {
        expr.accept(this, ctx);
        if (expr.type.noError() && !expr.type.eq(BuiltInType.BOOL)) {
            issue(new BadTestExpr(expr.pos));
        }
    }

    // Expressions

    @Override
    public void visitIntLit(Tree.IntLit that, ScopeStack ctx) {
        that.type = BuiltInType.INT;
    }

    @Override
    public void visitBoolLit(Tree.BoolLit that, ScopeStack ctx) {
        that.type = BuiltInType.BOOL;
    }

    @Override
    public void visitStringLit(Tree.StringLit that, ScopeStack ctx) {
        that.type = BuiltInType.STRING;
    }

    @Override
    public void visitNullLit(Tree.NullLit that, ScopeStack ctx) {
        that.type = BuiltInType.NULL;
    }

    @Override
    public void visitReadInt(Tree.ReadInt readInt, ScopeStack ctx) {
        readInt.type = BuiltInType.INT;
    }

    @Override
    public void visitReadLine(Tree.ReadLine readStringExpr, ScopeStack ctx) {
        readStringExpr.type = BuiltInType.STRING;
    }

    @Override
    public void visitUnary(Tree.Unary expr, ScopeStack ctx) {
        expr.operand.accept(this, ctx);
        var t = expr.operand.type;
        if (t.noError() && !compatible(expr.op, t)) {
            // Only report this error when the operand has no error, to avoid nested errors flushing.
            issue(new IncompatUnOpError(expr.pos, Tree.opStr(expr.op), t.toString()));
        }

        // Even when it doesn't type check, we could make a fair guess based on the operator kind.
        // Let's say the operator is `-`, then one possibly wants an integer as the operand.
        // Once he/she fixes the operand, according to our type inference rule, the whole unary expression
        // must have type int! Thus, we simply _assume_ it has type int, rather than `NoType`.
        expr.type = resultTypeOf(expr.op);
    }

    public boolean compatible(Tree.UnaryOp op, Type operand) {
        return switch (op) {
            case NEG -> operand.eq(BuiltInType.INT); // if e : int, then -e : int
            case NOT -> operand.eq(BuiltInType.BOOL); // if e : bool, then !e : bool
        };
    }

    public Type resultTypeOf(Tree.UnaryOp op) {
        return switch (op) {
            case NEG -> BuiltInType.INT;
            case NOT -> BuiltInType.BOOL;
        };
    }

    @Override
    public void visitBinary(Tree.Binary expr, ScopeStack ctx) {
        expr.lhs.accept(this, ctx);
        expr.rhs.accept(this, ctx);
        var t1 = expr.lhs.type;
        var t2 = expr.rhs.type;
        if (t1==null||t2==null) return;

        if (t1.noError() && t2.noError() && !compatible(expr.op, t1, t2)) {
            issue(new IncompatBinOpError(expr.pos, t1.toString(), Tree.opStr(expr.op), t2.toString()));
        }
        expr.type = resultTypeOf(expr.op);
    }

    public boolean compatible(Tree.BinaryOp op, Type lhs, Type rhs) {
        if (op.compareTo(Tree.BinaryOp.ADD) >= 0 && op.compareTo(Tree.BinaryOp.MOD) <= 0) { // arith
            // if e1, e2 : int, then e1 + e2 : int
            return lhs.eq(BuiltInType.INT) && rhs.eq(BuiltInType.INT);
        }

        if (op.equals(Tree.BinaryOp.AND) || op.equals(Tree.BinaryOp.OR)) { // logic
            // if e1, e2 : bool, then e1 && e2 : bool
            return lhs.eq(BuiltInType.BOOL) && rhs.eq(BuiltInType.BOOL);
        }

        if (op.equals(Tree.BinaryOp.EQ) || op.equals(Tree.BinaryOp.NE)) { // eq
            // if e1 : T1, e2 : T2, T1 <: T2 or T2 <: T1, then e1 == e2 : bool
            return lhs.subtypeOf(rhs) || rhs.subtypeOf(lhs);
        }

        // compare
        // if e1, e2 : int, then e1 > e2 : bool
        return lhs.eq(BuiltInType.INT) && rhs.eq(BuiltInType.INT);
    }

    public Type resultTypeOf(Tree.BinaryOp op) {
        if (op.compareTo(Tree.BinaryOp.ADD) >= 0 && op.compareTo(Tree.BinaryOp.MOD) <= 0) { // arith
            return BuiltInType.INT;
        }
        return BuiltInType.BOOL;
    }

    @Override
    public void visitNewArray(Tree.NewArray expr, ScopeStack ctx) {
        expr.elemType.accept(this, ctx);
        expr.length.accept(this, ctx);
        var et = expr.elemType.type;
        var lt = expr.length.type;

        if (et.isVoidType()) {
            issue(new BadArrElementError(expr.elemType.pos));
            expr.type = BuiltInType.ERROR;
        } else {
            expr.type = new ArrayType(et);
        }

        if (lt.noError() && !lt.eq(BuiltInType.INT)) {
            issue(new BadNewArrayLength(expr.length.pos));
        }
    }

    @Override
    public void visitNewClass(Tree.NewClass expr, ScopeStack ctx) {
        var clazz = ctx.lookupClass(expr.clazz.name);
        if (clazz.isPresent()) {
            //task-abstract-2
            if (clazz.get().isAbstract())
                issue(new NewAbstractError(expr.pos, clazz.get().name));
            else {
                expr.symbol = clazz.get();
                expr.type = expr.symbol.type;
            }
        } else {
            issue(new ClassNotFoundError(expr.pos, expr.clazz.name));
            expr.type = BuiltInType.ERROR;
        }
    }

    @Override
    public void visitThis(Tree.This expr, ScopeStack ctx) {
        if (ctx.currentMethod().isStatic()) {
            issue(new ThisInStaticFuncError(expr.pos));
        }
        expr.type = ctx.currentClass().type;
    }

    private boolean allowClassNameVar = false;

    @Override
    public void visitVarSel(Tree.VarSel expr, ScopeStack ctx) {
        if (expr.receiver.isEmpty()) {
            if (stk.contains(expr.name)) {
                issue(new UndeclVarError(expr.pos, expr.name));
                expr.type = BuiltInType.ERROR;
                return;
            }
            var symbol = ctx.lookupBefore(expr.name, localVarDefPos.orElse(expr.pos));
            if (symbol.isPresent()) {
                if (symbol.get().isVarSymbol()) {
                    var var = (VarSymbol) symbol.get();
                    expr.symbol = var;
                    expr.type = var.type;
                    if (var.isMemberVar()) {
                        if (ctx.currentMethod().isStatic()) {
                            issue(new RefNonStaticError(expr.pos, ctx.currentMethod().name, expr.name));
                        } else {
                            expr.setThis();
                        }
                    }
                    return;
                }

                if (symbol.get().isClassSymbol() && allowClassNameVar) { // special case: a class name
                    var clazz = (ClassSymbol) symbol.get();
                    expr.type = clazz.type;
                    expr.isClassName = true;
                    return;
                }
                if (symbol.get().isMethodSymbol()){
                    var method = (MethodSymbol)symbol.get();
                    if (ctx.currentMethod().isStatic() && !method.isStatic())
                        issue(new RefNonStaticError(expr.pos, ctx.currentMethod().name, expr.name));
                    expr.type = method.type;
                    return;
                }
            }
            expr.type = BuiltInType.ERROR;
            issue(new UndeclVarError(expr.pos, expr.name));
            return;
        }

        // has receiver
        var receiver = expr.receiver.get();

        allowClassNameVar = true;
        receiver.accept(this, ctx);
        allowClassNameVar = false;

        var rt = receiver.type;
        expr.type = BuiltInType.ERROR;

        if (receiver instanceof Tree.VarSel) {
            var v1 = (Tree.VarSel) receiver;
            if (v1.isClassName) {
                //不存在成员
                if (ctx.getClass(v1.name).scope.get(expr.name) == null){
                    issue(new FieldNotFoundError(expr.pos, expr.name, ((ClassType)rt).toString()));
                    return;
                }
                //成员是量和非静态函数无法通过类名访问
                var member = ctx.getClass(v1.name).scope.get(expr.name);
                if ( (member instanceof VarSymbol)
                    || !((MethodSymbol) member).isStatic()) {
                    // special case like MyClass.foo: report error cannot access field 'foo' from 'class : MyClass'
                        issue(new NotClassFieldError(expr.pos, expr.name, ((ClassType) rt).toString()));
                        return;
                }
            }
        }
        if (!rt.noError()) {
            return;
        }
        if (rt.isArrayType() && expr.name.equals("length")){
            ArrayList<Type> argList = new ArrayList<>();
            expr.type = new FunType(BuiltInType.INT, argList);
            return;
        }
        else if (!rt.isClassType()) {
            issue(new NotClassFieldError(expr.pos, expr.name, rt.toString()));
            return;
        }
        var ct = (ClassType) rt;
        var field = ctx.getClass(ct.name).scope.lookup(expr.name);
        if (field.isPresent() && field.get().isVarSymbol()) {
            var var = (VarSymbol) field.get();
            if (var.isMemberVar()) {
                expr.symbol = var;
                expr.type = var.type;
                if (!ctx.currentClass().type.subtypeOf(var.getOwner().type)) {
                    // member vars are protected

                    issue(new FieldNotAccessError(expr.pos, expr.name, ct.toString()));
                }
            }
        }
        else if (field.isPresent() && field.get().isMethodSymbol()){
            var method = (MethodSymbol) field.get();
            expr.type = method.type;
        }
        else if (field.isEmpty()) {
            issue(new FieldNotFoundError(expr.pos, expr.name, ct.toString()));
        } else {
            issue(new NotClassFieldError(expr.pos, expr.name, ct.toString()));
        }
    }

    @Override
    public void visitIndexSel(Tree.IndexSel expr, ScopeStack ctx) {
        expr.array.accept(this, ctx);
        expr.index.accept(this, ctx);
        var at = expr.array.type;
        var it = expr.index.type;
        if (at == null || it == null || at.hasError() || it.hasError()){
            expr.type = BuiltInType.ERROR;
            return;
        }
        if (!at.isArrayType()) {
            issue(new NotArrayError(expr.array.pos));
            expr.type = BuiltInType.ERROR;
            return;
        }

        expr.type = ((ArrayType) at).elementType;
        if (!it.eq(BuiltInType.INT)) {
            issue(new SubNotIntError(expr.pos));
        }
    }

    @Override
    public void visitCall(Tree.Call expr, ScopeStack ctx) {
        expr.type = BuiltInType.ERROR;
        expr.expr.accept(this, ctx);
        if (expr.expr.type==null || expr.expr.type.hasError()) return;

        if (! (expr.expr.type instanceof FunType)) {
            issue(new NotCallableTypeError(expr.pos, expr.expr.type.toString()));
            return;
        }

        typeCall(expr, (FunType)expr.expr.type, ctx);
        return;
    }

    private void typeCall(Tree.Call call, FunType type, ScopeStack ctx){
        call.type = type.returnType;
        var args = call.args;
        for (var arg : args) {
            arg.accept(this, ctx);
        }
        // check signature compatibility
        if (type.arity() != args.size()) {
            if (call.expr instanceof Tree.Call || call.expr instanceof Tree.Lambda)
                issue(new BadLambdaArgCountError(call.pos, type.arity(), args.size()));
            else if (call.expr instanceof Tree.VarSel){
                issue(new BadArgCountError(call.pos, ((Tree.VarSel)call.expr).name, type.arity(), args.size()));
            }
            else {
                System.out.println(call);
                issue(new BadArgCountError(call.pos, call.symbol.name, type.arity(), args.size()));
            }
        }

        var iter1 = type.argTypes.iterator();
        var iter2 = call.args.iterator();
        for (int i = 1; iter1.hasNext() && iter2.hasNext(); i++) {
            Type t1 = iter1.next();
            Tree.Expr e = iter2.next();
            Type t2 = e.type;
            if (t2.noError() && !t2.subtypeOf(t1)) {
                issue(new BadArgTypeError(e.pos, i, t2.toString(), t1.toString()));
            }
        }
    }

    @Override
    public void visitClassTest(Tree.ClassTest expr, ScopeStack ctx) {
        expr.obj.accept(this, ctx);
        expr.type = BuiltInType.BOOL;

        if (!expr.obj.type.isClassType()) {
            issue(new NotClassError(expr.obj.type.toString(), expr.pos));
        }
        var clazz = ctx.lookupClass(expr.is.name);
        if (clazz.isEmpty()) {
            issue(new ClassNotFoundError(expr.pos, expr.is.name));
        } else {
            expr.symbol = clazz.get();
        }
    }

    @Override
    public void visitClassCast(Tree.ClassCast expr, ScopeStack ctx) {
        expr.obj.accept(this, ctx);

        if (!expr.obj.type.isClassType()) {
            issue(new NotClassError(expr.obj.type.toString(), expr.pos));
        }

        var clazz = ctx.lookupClass(expr.to.name);
        if (clazz.isEmpty()) {
            issue(new ClassNotFoundError(expr.pos, expr.to.name));
            expr.type = BuiltInType.ERROR;
        } else {
            expr.symbol = clazz.get();
            expr.type = expr.symbol.type;
        }
    }

    @Override
    public void visitLocalVarDef(Tree.LocalVarDef stmt, ScopeStack ctx) {
        if (stmt.initVal.isEmpty()) return;

        var initVal = stmt.initVal.get();
        if (initVal instanceof Tree.Lambda){ stk.push(stmt.name);}

        localVarDefPos = Optional.ofNullable(stmt.id.pos);
        initVal.accept(this, ctx);
        localVarDefPos = Optional.empty();

        if (initVal instanceof Tree.Lambda){stk.pop();}

        if (initVal.type == null) return; //ab-er-3

        if (stmt.symbol.type != null) {
            var lt = stmt.symbol.type;
            var rt = initVal.type;

            if (lt.noError() && !rt.subtypeOf(lt)) {
                issue(new IncompatBinOpError(stmt.assignPos, lt.toString(), "=", rt.toString()));
            }
        }
        //task-var
        else if (initVal.type.isVoidType()) {
            issue(new BadVarTypeError(stmt.pos, stmt.id.name));
        } else {
            var symbol = new VarSymbol(stmt.symbol.name, initVal.type, stmt.symbol.pos);
            ctx.declare(symbol);
        }
    }

    @Override
    public void visitLambda(Tree.Lambda lambda, ScopeStack ctx) {
        var scope = lambda.symbol.scope;
        typeLambda(lambda, ctx, scope);
        var symbol = new LambdaSymbol((FunType) lambda.type, lambda.symbol.scope, lambda.symbol.pos);
        ctx.declare(symbol);
        lambda.symbol = symbol;
    }
    private void typeLambda(Tree.Lambda lambda, ScopeStack ctx, LambdaScope lambdaScope){
        ctx.open(lambdaScope);
        var argTypes = new ArrayList<Type>();
        for (var param : lambda.varList) {
            argTypes.add(param.typeLit.get().type);
        }
        if (lambda.expr != null){
            ctx.open(lambdaScope.nestedLocalScope());
            lambda.expr.accept(this, ctx);
            ctx.close();
            lambda.type = new FunType(lambda.expr.type, argTypes);
        }
        else{
            lambda.block.accept(this, ctx);
            if (lambda.block.returnTypes.size() >= 1 && !lambda.block.returns) {
                var flag = false;
                for (var t : lambda.block.returnTypes){
                    if (!t.isVoidType()) flag = true;
                }
                if (flag)
                    issue(new MissingReturnError(lambda.block.pos));
            }
            Tree.Block block = lambda.block;
            if (!block.returnTypes.isEmpty()) {
                Pos pos = ctx.currentLambda() != null ? ctx.currentLambda().scope.nestedLocalScope().block.pos : ctx.currentMethod().pos;
                block.type = typeBound(block.returnTypes, pos, true);
            }
            lambda.type = lambda.block.type == null ? null : new FunType(lambda.block.type, argTypes);
        }
        ctx.close();
    }
    // Only usage: check if an initializer cyclically refers to the declared variable, e.g. var x = x + 1
    private Optional<Pos> localVarDefPos = Optional.empty();
}
