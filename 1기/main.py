from flask import Flask, render_template, url_for, request, make_response
import pymysql
import json
import simplejson

app = Flask(__name__)

@app.route('/')
def index():
    labels = []
    cost = []
    tax = []
    try:
        sample_db = pymysql.connect(
            user='root',
            passwd='1234',
            host='localhost',
            db='test'
        )
        cursor = sample_db.cursor()
        sql = "select * from chart"
        cursor.execute(sql) 
        # sql구문이 실행
        result=cursor.fetchall()
        for list in result:
            labels.append(list[0])
            cost.append(list[1])
            tax.append(list[2])
    finally:
        sample_db.close()

    try:
        sample_db = pymysql.connect(
            user='root',
            passwd='1234',
            host='localhost',
            db='test'
        )
        cursor = sample_db.cursor()
        sql = "select * from chart limit 1"
        cursor.execute(sql) 
        # sql구문이 실행
        result2=cursor.fetchall()
    finally:
        sample_db.close()
  
    print(result)      
    print(result2)
    return render_template('index.html', result=result, label=labels, data1=cost, data2=tax)

@app.route('/dy')
def dy():
    a = {
        "name" : "moon",
        "age" : "37"
        }
    return a

@app.route('/chart')
def chart():
    gragh_data = {}
    i = 0
    try:
        sample_db = pymysql.connect(
            user='root',
            passwd='1234',
            host='localhost',
            db='test'
        )
        cursor = sample_db.cursor()
        sql = "SELECT abs(DAYS_BIRTH) as x, income_total as y FROM train limit 30;"
        cursor.execute(sql)
        # result2 = cursor.fetchall()
        # result = json.dumps(result2)
        r = [dict((cursor.description[i][0], value)                
        for i, value in enumerate(row)) 
        for row in cursor.fetchall()]
    finally:
        sample_db.close()
    result = json.dumps(r, ensure_ascii=False)
    res = make_response(result)
    print(result)
    return render_template('dash_.html', result=result)

@app.route('/pasing')
def pasing():
    a = []
    b =[]
    try:
        sample_db = pymysql.connect(
            user='root',
            passwd='1234',
            host='localhost',
            db='web_test'
        )
        cursor = sample_db.cursor()
        sql = "SELECT occyp_type, COUNT(occyp_type) AS cnt FROM train group by occyp_type;"
        cursor.execute(sql)
        result=cursor.fetchall()
        for list in result:
            if list[0]:
                b.append(list[0])
                a.append(list[1])
            else:
                b.append('empty')
                a.append(list[1])
        print(b)
    finally:
        sample_db.close()
    return render_template('pasing.html', result=result, a = a, b=b)

@app.route('/scatter')
def scatter():
    try:
        sample_db = pymysql.connect(
            user='root',
            passwd='1234',
            host='localhost',
            db='test'
        )
        cursor = sample_db.cursor()
        sql = "SELECT abs(DAYS_BIRTH)/365, income_total  FROM train;"
        cursor.execute(sql)
        result2 = cursor.fetchall();
        result = simplejson.dumps(result2)
        r = [dict((cursor.description[i][0], value)                
        for i, value in enumerate(row)) 
        for row in cursor.fetchall()]
        print(r)
    finally:
        sample_db.close()
    return render_template('scatter.html', result=result, result2=result2)

@app.route('/ajax')
def ajax():
    return render_template('ajax.html')

@app.route('/ajax_get', methods=["GET"])
def ajax_get():
    _message = request.args["message"]
    print(_message)
    answer = []
    answer.append({"data1":_message})
    return json.dumps(answer)

@app.route('/ajax_post', methods=["POST"])
def ajax_post():
    _message = request.form["message"]
    print(_message)
    answer = []
    if _message == "asd":
        answer.append({"data1" : "Key 값이 일치"})
    else:
        answer.append({"data1" : "Key 값 불일치"})
    return json.dumps(answer)

@app.route('/get_json')
def get_json():
    _message = request.args["message"]
    try:
        sample_db = pymysql.connect(
            user='root',
            passwd='1234',
            host='localhost',
            db='web_test'
        )
        cursor = sample_db.cursor()
        sql = "select * from test where No = %s"
        val = (_message)
        cursor.execute(sql, val)
        result=cursor.fetchall()
        list2 = [];
        for list in result:
            list[0].remove
        
        # sql구문이 실행
    finally:
        sample_db.close()
    print(json.dumps(result).append(result2))
    return json.dumps(result)

app.run


# data type --> ()튜플    {}딕셔너리    []리스트