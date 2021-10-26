
import psycopg2
from config import config
from flask import Flask, jsonify, request, render_template, abort, url_for, json
import os
import json
import html

# def get_parts():
    # """ query parts from the parts table """
conn = None

try:
    params = config()
    conn = psycopg2.connect(**params)
        # cur = conn.cursor()
        # cur.execute("SELECT * FROM category2")
        # rows = cur.fetchall()
        # print("The number of parts: ", cur.rowcount)
        # for row in rows:
        #     print(row)
        # cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()

cur = conn.cursor()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/v_timestamp')
def v_timestamp():
    cur.execute("SELECT * FROM category2")
    data = cur.fetchall()
    rowarray_list=[]
    for row in data:
        t = (row[0], row[1], row[2], row[3])
        rowarray_list.append(t)
    j = json.dumps(rowarray_list, default=str)
    print(j)    
    return render_template('v_timestamp.html', data=j)

if __name__ == "__main__":
    app.run(debug=True)


# article to display data https://kanchanardj.medium.com/how-to-display-database-content-in-your-flask-website-8a62492ba892
# querying data from postgresql https://www.postgresqltutorial.com/postgresql-python/query/

