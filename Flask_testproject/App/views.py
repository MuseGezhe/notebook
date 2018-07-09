from flask import Blueprint, render_template, request, redirect, abort, url_for
from flask_login import login_user, login_required, current_user, logout_user

from App import files
from App.ext import lm, db
from App.forms import RegistrationForm, UpdateForm
from App.models import User,Movie

blue = Blueprint("first",__name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)


@lm.user_loader
def user_loader(id):
    user = User.query.filter_by(id=id).first()
    return user



# 主页
@blue.route("/home/")
def to_news():
    page = int(request.args.get("page") or 1)
    pagination = Movie.query.order_by('-online_time').paginate(page,3,False)
    return  render_template("movies.html.",pagination=pagination)


@blue.route("/toLogin/")
def to_login():
    return render_template("login.html")

# 登录
@blue.route("/login/",methods=["POST","GET"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        pwd = request.form.get("pwd")
        user = User.query.filter_by(name=name,pwd=pwd).first()
        if user:
            login_user(user)
            return redirect("/admin/")
    return render_template("login.html")

# 个人中心
@blue.route("/admin/")
@login_required
def admin():
    user = current_user
    pic_path = url_for('static', filename=user.pic)
    return render_template("userinfo.html", user=user, pic_path=pic_path)


# 修改个人信息
@blue.route("/update/",methods=["GET","POST"])
def update():
    form = UpdateForm()
    if form.validate_on_submit():
        user = current_user
        user.pwd = form.pwd.data
        user.pic = files.file_save(form)

        db.session.add(user)
        db.session.commit()
        return redirect("/admin/")
    return render_template("update.html",form=form)


# 退出
@blue.route("/loginout/")
def login_out():
    if current_user:
        user = current_user
        msg = "{}您确定要退出？".format(user.name)
        logout_user()
        return render_template("quit.html",msg=msg)
    return render_template("login.html")


@blue.route("/safeuser/")
@login_required
def user_validate():
    return "只有合法用户才能访问的内容"

# 注册
@blue.route("/register/",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data,pwd=form.pwd.data)
        # 获取该用户下的图片
        user.pic = files.file_save(form)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            msg = "未知错误{}".format(e)
            db.session.rollback()
            abort(500,msg)
        return redirect(url_for("first.login"))
    return render_template("register.html",form=form)


@blue.route("/desc/")
def desc():
    video = request.args.get("mid")
    desc = Movie.query.get(video)
    return render_template("desc.html",desc=desc)

@blue.route("/drop/")
def drop():
    video = request.args.get("mid")
    desc = Movie.query.get(video)
    db.session.delete(desc)
    db.session.commit()
    return redirect('/home/')