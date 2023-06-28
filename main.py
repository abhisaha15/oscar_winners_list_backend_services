from flask import Flask,jsonify
import sqlite3
import os
import json
from flask_cors import CORS, cross_origin

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('oscar_db.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
@app.route('/<string:year>')
@cross_origin()
def home(year="2023"):
    conn = get_db_connection()
    if (year.isdigit()==False):
        year = 2023
    elif(year.isdigit()==True and (len(year)<3 or len(year)>5)):
        year = 2023
    else:
        year = str(year)
    d_a_t_a = conn.execute('SELECT * FROM oscar_data WHERE year = {}'.format(year)).fetchall()
    conn.close()
    winner_list = ''
    for i in d_a_t_a:
        winner_list = json.loads(str(i[2]))

    return json.loads(winner_list)





if __name__ == "__main__":
    app.run(debug=True)
