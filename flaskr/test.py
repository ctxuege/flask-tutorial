from flask import (
    session,render_template,g,redirect,url_for,Blueprint,request
)


bp = Blueprint("test",__name__,url_prefix="/test")


@bp.route('/ces1',methods=["POST","GET"])
def login_test_index():
    if request.method == "GET":
        return render_template("test/register.html")
    else:
        return "hello , test"