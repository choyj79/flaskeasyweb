import os #os모듈 추가
from flask_mail import Mail, Message
from flask import Flask, render_template, url_for, redirect, request, flash
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)

#secret_key추가
app.config["SECRET_KEY"] = b"\xfd_@E\x17\xd8'\xf6e-\xff\xe4\xa2MC2"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jojju486@gmail.com'
app.config['MAIL_PASSWORD'] = 'stkm cgck saeq hlju'

mail = Mail(app)

@app.route("/")
def index():
    return 'Hello, 성공!!!'

@app.route("/hello/<name>",methods=["GET"],endpoint='hello-enepoint')
def hello(name):
    return f"hello!! {name}!!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html",name=name)

def send_email(to, subject, template, **kwargs):    
    """메일을 송신하는 함수"""
    msg = Message(subject, sender='jojju486@gmail.com', recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)

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

        is_valid = True

        if not username:
            flash("사용자명은 필수입니다")
            is_valid = False

        if not email:
            flash("메일 주소는 필수입니다")
            is_valid = False
        
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("메일 주소의 형식으로 입력해 주세요")
            is_valid = False
        
        if not description:
            flash("문의 내용은 필수입니다")
            is_valid = False
        
        if not is_valid:
            return redirect(url_for("contact"))
        
        send_email(
            email,
            "문의 감사합니다.",
            "contact_mail",
            username = username,
            description = description
        )
        flash("문의 내용은 메일로 송신했습니다. 문의해 주셔서 감사합니다.")
        
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

with app.test_request_context():
    print(url_for("index"))
    print(url_for("show_name",name='choyj',page = 1))
    print(url_for("index"))  