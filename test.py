from datetime import date

from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'sql5685964'
app.config['MYSQL_PASSWORD']='AWbjgyPIUX'
app.config['MYSQL_HOST']='sql5.freemysqlhosting.net'
app.config['MYSQL_DB']='sql5685964'
# app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    # cur.execute('''CREATE TABLE employees (name VARCHAR(50),date DATE)''')
    cur.execute('''INSERT INTO employees VALUES ('Karl', '2005-10-22')''')
    cur.execute('''INSERT INTO employees VALUES ('Max','2006-11-22')''')
    mysql.connection.commit()
    cur.close()
    return "done!"

    # cur.execute('''SELECT * FROM example''')
    # results = cur.fetchall()
    # print(results)
    # return 'Done!'
#     cur.execute('''CREATE PROCEDURE multiply(IN pFac1 INT, IN pFac2 INT, OUT pProd INT)
# BEGIN
#   SET pProd := pFac1 * pFac2;
# END;''')

    # cur.callproc('getusers')
    # print(cur.fetchall())
    # data = [
    #     ('Jane', date(2005, 2, 12)),
    #     ('Joe', date(2006, 5, 23)),
    #     ('John', date(2010, 10, 3)),
    # ]
    #
    # stmt = "INSERT INTO employees (name, date) VALUES (%s, %s)"
    # cur.executemany(stmt, data)
    # mysql.connection.commit()
    #
    # cur.execute('''SELECT * FROM employees''')
    # results = cur.fetchmany(size=2)
    # print(results)
    # return 'done!'

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)