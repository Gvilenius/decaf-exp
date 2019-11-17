package decaf.driver.error;

import decaf.frontend.tree.Pos;

public class IncompatReturnTypesError extends DecafError{
    public IncompatReturnTypesError(Pos pos){
        super(pos);
    }
    @Override
    public String getErrMsg() {
        return "incompatible return types in blocked expression";
    }
}
