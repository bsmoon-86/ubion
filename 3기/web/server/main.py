from  flask import Flask

app = Flask(__name__)

@app.route('/')         #web -> 주소 -> 127.0.0.1:5000/, localhost:5000/
def index():
    return "Hello, World"

#url을 추가해서 def를 실행을 하려면? 어떻게??

@app.route('/second/')   #web -> address -> 127.0.0.1:5000/second/
def second():
    return "Second Page"

app.run