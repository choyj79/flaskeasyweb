from flask import Flask, Blueprint, render_template, redirect, url_for,flash, request
from app import db
from apps.board.models import Board
from apps.board.forms import BoardForm
from flask_login import login_user, logout_user

#blueprint로 crud 앱을 생성
board = Blueprint(
    "board", 
    __name__, 
    template_folder="templates",
    static_folder="static"
)

@board.route("/")
def index():
    board = Board.query.all()
    return render_template("board/index.html", board = board)

@board.route("/board/new", methods=["GET", "POST"])
def create_user(user_id):
    # UserForm을 인스턴스화한다
    form = BoardForm()

    # 폼의 값을 벨리데이트한다
    if form.validate_on_submit():
        # 사용자를 작성한다
        board = Board(
            title=form.title.data,
            content=form.content.data,
        )

        # 사용자를 추가하고 커밋한다
        db.session.add(board)
        db.session.commit()

        # 사용자의 일람 화면으로 리다이렉트한다
        return redirect(url_for("auth.users"))
    return render_template("auth/create.html", form=form)

# @board.route("/board")
# def edit_user(user_id):
#     form = UserForm()
#     user = User.query.filter_by(id=user_id).first()
#     if form.validate_on_submit():
#         user.username = form.username.data
#         user.email = form.email.data
#         user.password = form.password.data
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('crud.users'))
#     return render_template('crud/edit.html',user=user, form=form)
