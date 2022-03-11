from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

#localhost로 접속했을때
@app.route("/")
def index():
    return render_template("index.html")

#localhost/signup로 접속했을때
@app.route("/signup/", methods=["GET"])
def signup():
    return render_template("signup.html")
@app.route("/signup", methods=["POST"])
def signup_2():
    _db = pymysql.connect(
        user = "root",
        passwd = "1234",
        host = "localhost",
        db = "ubion"
    )
    cursor = _db.cursor()
    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _ads = request.form["_ads"]
    _regitdate = request.form["_regitdate"]
    sql = """
            INSERT INTO user_info VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s)
        """
    _values = [_id, _password, _name, _phone, _ads, _gender, _age, _regitdate]
    cursor.execute(sql, _values)
    _db.commit()
    _db.close()

    # print(request.form)
    return redirect(url_for('index'))


app.run(port=80)