from flask import Flask, Blueprint, render_template, redirect, url_for,flash, request
from app import db
from apps.board.models import Board
# from apps.board.forms import BoardForm
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
    return render_template("board/index.html")

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
