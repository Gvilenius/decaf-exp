package decaf.driver.error;

import decaf.frontend.tree.Pos;

public class VarError extends DecafError{
    private String id;

    public VarError(Pos pos, String id) {
        super(pos);
        this.id = "'" + id + "'";
    }

    @Override
    protected String getErrMsg() {
        return  "cannot declare identifier " + id + " as void type";
    }
}

