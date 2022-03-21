from flask import Flask, request, render_template
from modules import mod_sql
import json
import simplejson

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    _db = mod_sql.Database()
    _sql = """
            SELECT * FROM user_info
        """
    result = _db.executeAll(_sql)
    print(json.dumps(result))
    return json.dumps(result)


app.run(debug=True)
