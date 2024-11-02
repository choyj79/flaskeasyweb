from flask import Flask, Blueprint, render_template, redirect, url_for,flash, request
from app import db
from apps.crud.models import User
from apps.acct.forms import SignUpForm, LoginForm
from flask_login import login_user, logout_user

#blueprint로 crud 앱을 생성
acct = Blueprint(
    "acct", 
    __name__, 
    template_folder="templates",
    static_folder="static"
)

@acct.route("/")
def index():
    return render_template("acct/index.html")

@acct.route("/signup", methods=["GET","POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # 사용자를 작성한다
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        #메일 중복 체크
        if user.is_duplicate_email():
            flash("지정한 이메일 주소는 이미 등록되어 있습니다.")
            return redirect(url_for("acct.signup"))
        
        #사용자 정보 등록
        db.session.add(user)
        db.session.commit()
        print("!!!!!!!!!!!!!!!!!!!!!!!!aaaaaaa",user)
        # 사용자 정보를 세션에 저장한다
        login_user(user)

        # GET 파라미터에 next 키가 존재하고, 값이 없는 경우는 사용자의 일람 페이지로 리다이렉트한다
        next_ = request.args.get("next")
        if next_ is  None and not next_.startswith("/"): 
            next_ = url_for("crud.users")
        print("next!!!!!!!!!!!!!!!!!!!!!",next_)
        return redirect(next_)

    return render_template("acct/signup.html", form=form)
@acct.route("/login",methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 메일주소로 사용자 가져오기
        user = User.query.filter_by(email=form.email.data).first()
        #사용자가 존재하고 비밀번호가 일치하면 로그인
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('crud.users'))
        flash("메일 주소 또는 비밀번호가 일치하지 않습니다.")
    return render_template("acct/login.html",form=form)

@acct.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("acct.login"))