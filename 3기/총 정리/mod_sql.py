# sql 모듈 생성
# 1. Class 생성 Database
# 2. Class 생성이 될때 pymysql.connect 변수 생성, cursor 생성 (__init__)
# 3. init을 제외한 함수 3개 생성
# 4. execute() -> sql, value를 받아와서 sql문을 실행.
# 5. executeAll() -> sql, value 받아와서 sql문을 실행을 하고 결과값을 return
# 6. commit() -> commit을 하는 함수.
# 7. execute(), executeAll()함수에서 value 값은 디폴트 {} 값 지정
# 8. main.py 모듈을 load해서 기존에 sql 작업을 모듈을 사용해서 코드를 작성 
import pymysql

class Database():
    def __init__(self):
        self._db = pymysql.connect(host = 'localhost',
                                   user = 'root',
                                   password = "1234",
                                   db = "ubion",
                                   port = 3306)
        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)
    
    def execute(self, _sql, _values={}):
        self.cursor.execute(_sql, _values)

    def executeAll(self, _sql, _values={}):
        self.cursor.execute(_sql, _values)
        self.result = self.cursor.fetchall()
        return self.result

    def commit(self):
        self._db.commit()
