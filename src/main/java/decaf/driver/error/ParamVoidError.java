package decaf.driver.error;

import decaf.frontend.tree.Pos;

public class ParamVoidError extends DecafError {
    public ParamVoidError(Pos pos) {
        super(pos);
    }

    @Override
    protected String getErrMsg() {
        return "arguments in function type must be non-void known type";
    }
}
