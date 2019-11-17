package decaf.driver.error;

import decaf.frontend.tree.Pos;

public class LambdaAssignVarOutOfScopeError extends DecafError{
    public LambdaAssignVarOutOfScopeError(Pos pos) {
        super(pos);
    }

    @Override
    protected String getErrMsg() {
        return "cannot assign value to captured variables in lambda expression";
    }
}
