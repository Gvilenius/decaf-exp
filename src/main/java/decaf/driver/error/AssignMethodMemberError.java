package decaf.driver.error;

import decaf.frontend.tree.Pos;

public class AssignMethodMemberError extends DecafError {
    String method;
    public AssignMethodMemberError(Pos pos,String method){
        super(pos);
        this.method = "'" + method + "'";
    }
    @Override
    protected String getErrMsg() {
        return "cannot assign value to class member method " + method;
    }
}
