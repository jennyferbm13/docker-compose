

import mysql.connector
from flask import Flask

app = Flask(__name__)
db = mysql.connector.connect(host="mysql", user ="Pelusa", password="goku")
cache=db.cursos()
if len(cache.execute("SHOW TABLES")) == 0:
  cache.execute("CREATE TABLE info (hits TINYINT(100))")
  sql = "INSERT INTO info (hits) VALUES (%d)"
  val =0
  try:
    cache.execute(sql,val)
    db.commit()
  except mysql.connector.Error as err:
    print(err)
    print("Error Code:", err.errno)
    print("SQLSTATE", err.msg)
    

def get_hit_count():
    retries = 5
    while True:
        cache.execute("SELECT * FROM info)
        hits = cache.fetchone()+1
        try:
            cache.execute("UPDATE info SET hits=(%d)", hits)
            db.commit()
            return hits
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.msg)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
