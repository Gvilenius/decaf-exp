package decaf.frontend.scope;

import decaf.frontend.tree.Tree;

import java.util.ArrayList;
import java.util.List;

/**
 * Local scope: stores locally-defined variables.
 */
public class LocalScope extends Scope {

    public LocalScope(Scope parent) {
        super(Kind.LOCAL);
//        assert parent.isFormalOrLocalScope();
        if (parent.isFormalScope()) {
            ((FormalScope) parent).setNested(this);
            this.parent = parent;
        }
        else if (parent.isLambdaScope()) {
            ((LambdaScope) parent).setNested(this);
            this.parent = parent;
        }
        else {
            ((LocalScope) parent).nested.add(this);
            this.parent = parent;
        }
    }

    @Override
    public boolean isLocalScope() {
        return true;
    }

    public boolean have(String key){
        if (symbols.containsKey(key)){
            return true;
        }
        else if (parent instanceof LocalScope) {
            return (((LocalScope) parent).have(key));
        }
        else if (parent instanceof LambdaScope){
            return ((LambdaScope) parent).have(key);
        }
        return false;
    }
    /**
     * Collect all local scopes defined inside this scope.
     *
     * @return local scopes
     */
    public List<Scope> nestedLocalScopes() {
        return nested;
    }

    private Scope parent;
    public List<Scope> nested = new ArrayList<>();
    public Tree.Block block;
}
