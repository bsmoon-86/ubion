from flask import Flask, render_template, url_for
import pymysql
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
            db='web_test'
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
        print(result)
    finally:
        sample_db.close()

    return render_template('index.html', result=result, label=labels, data1=cost, data2=tax)

@app.route('/dy')
def dy():
    return render_template('dygragh.html')

@app.route('/chart')
def chart():
    labels = []
    cost = []
    tax = []
    try:
        sample_db = pymysql.connect(
            user='root',
            passwd='1234',
            host='localhost',
            db='web_test'
        )
        cursor = sample_db.cursor()
        sql = "select * from chart"
        cursor.execute(sql)
        result=cursor.fetchall()
        for list in result:
            labels.append(list[0])
            cost.append(list[1])
            tax.append(list[2])
        print(result)
        print(labels)
        print(cost)
        print(tax)
    finally:
        sample_db.close()
    return render_template('dash.html', result=result, labels=labels, cost=cost, tax=tax)

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
            db='web_test'
        )
        cursor = sample_db.cursor()
        sql = "SELECT abs(DAYS_BIRTH)/365, income_total  FROM train;"
        cursor.execute(sql)
        result2 = cursor.fetchall();
        result = simplejson.dumps(result2)
        print(result2)
    finally:
        sample_db.close()
    return render_template('scatter.html', result=result, result2=result2)

app.run


# data type --> ()튜플    {}딕셔너리    []리스트