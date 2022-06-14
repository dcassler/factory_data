from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'db'
mysql = MySQL(app)

@app.route('/all_sprocket')
def all_allsproket():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM  factory_data")
    mysql.connection.commit()
    rv = cur.fetchall()
    return str(rv)


@app.route('/given_factory_id')
def given_factory_id():
    cur = mysql.connection.cursor()
    factory_id = request.args.get("factory_id")
    print(factory_id)
    sql_statement = "SELECT * FROM factory_data WHERE factory_id = "+ factory_id
    cur.execute(sql_statement)
    mysql.connection.commit()
    rv = cur.fetchall()
    return str(rv)

@app.route('/given_sprocket_id', methods=['GET'])
def given_sprocket_id():
    return 0


@app.route('/create_new_sprocket', methods=['POST'])
def create_new_sprocket():
    return 0


@app.route('/update_sprocket', methods=['PUT'])
def update_sprocket():
    return 0