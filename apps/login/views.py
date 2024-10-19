from flask import Flask, Blueprint, render_template, redirect, url_for,flash, request
from apps.app import db
from apps.crud.models import User
from apps.login.forms import SignUpForm
from flask_login import login_user, logout_user

#blueprint로 crud 앱을 생성
login = Blueprint(
    "login", 
    __name__, 
    template_folder="templates",
    static_folder="static"
)

@login.route("/")
def index():
    return render_template("login/index.html")

@login.route("/signup", methods=["GET","POST"])
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
            return redirect(url_for("login.signup"))
        
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

    return render_template("login/signup.html", form=form)

# @login.route("/login",method=["GET","POST"])
# def login():
#     form = LoginForm