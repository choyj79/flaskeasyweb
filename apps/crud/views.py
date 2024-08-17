from flask import Flask, Blueprint, render_template

#blueprint로 crud 앱을 생성
crud = Blueprint(
    "crud", 
    __name__, 
    template_folder="templates",
    static_folder="static"
)

@crud.route("/")
def index():
    print("!!!!!!!!!!!")
    return render_template("crud/index.html")
