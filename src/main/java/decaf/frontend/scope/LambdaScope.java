package decaf.frontend.scope;

import decaf.backend.dataflow.Loc;
import decaf.frontend.symbol.LambdaSymbol;
import decaf.frontend.symbol.Symbol;
import decaf.frontend.tree.Tree;

import java.util.ArrayList;
import java.util.List;


public class LambdaScope extends Scope {

    private LambdaSymbol owner;

    public void setOwner(LambdaSymbol owner){
        this.owner = owner;
    }

    public LambdaSymbol getOwner(){
        return owner;
    }

    public boolean have(String key){
        return (symbols.containsKey(key));
    }

    public LambdaScope(LocalScope parent) {
        super(Kind.LAMBDA);
        parent.nested.add(this);
    }

    @Override
    public boolean isLambdaScope() {
        return true;
    }

    /**
     * Collect all local scopes defined inside this scope.
     *
     * @return local scopes
     */
    public LocalScope nestedLocalScope() {
        return nested;
    }

    public void setNested(LocalScope scope){nested = scope;}

    private LocalScope nested = new LocalScope(this);
}
