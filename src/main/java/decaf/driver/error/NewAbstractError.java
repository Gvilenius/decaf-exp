package decaf.driver.error;

import decaf.frontend.tree.Pos;

public class NewAbstractError extends DecafError{
    private String className;

    public NewAbstractError(Pos pos, String className) {
        super(pos);
        this.className = "'" + className + "'";
    }

    @Override
    protected String getErrMsg() {
        return  "cannot instantiate abstract class " + className;
    }
}

