from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello, 성공!!!'

@app.route("/hello/<name>",methods=["GET"],endpoint='hello-enepoint')
def hello(name):
    return f"hello!! {name}!!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html",name=name)
## 문의 폼############
@app.route("/contact")
def contact():
    return render_template("contact.html")

##문의 완료 폼##############
@app.route("/contact_complete", methods=["GET","POST"])
def contact_complete():
    if request.method == "POST":
        #html의 form 속성에서 값을 가져오는 부분
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]
        
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

with app.test_request_context():
    print(url_for("index"))
    print(url_for("show_name",name='choyj',page = 1))
    print(url_for("index"))  