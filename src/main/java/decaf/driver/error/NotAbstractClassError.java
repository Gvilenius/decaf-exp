package decaf.driver.error;

import decaf.frontend.tree.Pos;

public class NotAbstractClassError extends DecafError {

    private String className;

    public NotAbstractClassError(Pos pos, String className) {
        super(pos);
        this.className = "'" + className + "'";
    }

    @Override
    protected String getErrMsg() {
        return className + " is not abstract and does not override all abstract methods";
    }

}