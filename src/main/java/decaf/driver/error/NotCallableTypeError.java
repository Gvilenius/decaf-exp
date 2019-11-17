package decaf.driver.error;

import decaf.frontend.tree.Pos;

public class NotCallableTypeError extends DecafError {
    String type;
    public NotCallableTypeError(Pos pos, String type){
        super(pos);
        this.type = type;
    }
    @Override
    protected String getErrMsg() {
        return type + " is not a callable type";
    }
}
