from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'db'
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

@app.route('/given_sprocket_id')
def given_sprocket_id():
    cur = mysql.connection.cursor()
    sprocket_id = request.args.get("sprocket_id")
    print(sprocket_id)
    sql_statement = "SELECT * FROM sprocket_data WHERE sprocket_id = "+ sprocket_id
    cur.execute(sql_statement)
    mysql.connection.commit()
    rv = cur.fetchall()
    return str(rv)


@app.route('/create_new_sprocket', methods=['POST'])
def create_new_sprocket():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        print(json) 
    else:
        return 'Content-Type not supported!'
    cur = mysql.connection.cursor()
    sql_statement = "INSERT INTO db.sprocket_data (sprocket_id, teeth, pitch_diameter, outside_diameter, pitch) VALUES({0},{1},{2},{3},{4});".format(json["sprocket_id"], json["teeth"], json["pitch_diameter"], json["outside_diameter"], json["pitch"])
    cur.execute(sql_statement)
    mysql.connection.commit()
    cur.close()
    return f"Done!!"

@app.route('/update_sprocket', methods=['PUT'])
def update_sprocket():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        print(json) 
    else:
        return 'Content-Type not supported!'
    cur = mysql.connection.cursor()
    sql_statement = "UPDATE db.sprocket_data SET teeth={0}, pitch_diameter={1}, outside_diameter={2}, pitch={3} WHERE sprocket_id={4};".format(json["teeth"], json["pitch_diameter"], json["outside_diameter"], json["pitch"], json["sprocket_id"])
    cur.execute(sql_statement)
    mysql.connection.commit()
    cur.close()
    return f"Done!!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)