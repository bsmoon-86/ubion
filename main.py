from flask import Flask, render_template, url_for
import pymysql

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

app.run


# data type --> ()튜플    {}딕셔너리    []리스트