from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/second/')
def second():
    _id = request.args.get("id")
    _pass = request.args.get("pass")
    # print(request)
    return render_template("second.html", id = _id, _pass = _pass)
    # if _id == "asd" and _pass == "qwe":
    #     return render_template("second.html")
    # else:
    #     return "로그인에 실패하였습니다"
        # return render_template("")

@app.route('/third/', methods=['POST'])
def third():
    _id = request.form['id']
    _pass = request.form['pass']
    print(request.args)
    return "Hello"

app.run