#!/usr/bin/env python
"""
Sample Flask App
"""
import os.path
from flask import Flask
from flask import jsonify
from flask import request
from healthcheck import HealthCheck
app = Flask(__name__)

health = HealthCheck()

app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())


def write_user(name,surname):
    """
    Write User
    """
    if os.path.isfile('./users.txt'):
        with open('./users.txt', 'a',encoding='utf_8') as file:
            file.write(f'{name}:{surname}\n')
    else:
        with open('./users.txt', 'w',encoding='utf_8') as file:
            file.write(f'{name}:{surname}\n')
    return True

@app.route('/',methods=['GET'])
def home():
    """
    Return Default Value
    """
    return jsonify(
      firstname='oguzhalit',
      lastname='sak'
    )
@app.route('/whoami',methods=['GET','POST'])
def get_user():
    """
    Send User with Parameters
    """
    if request.method == 'GET':
        fname=request.args.get('firstname')
        lname=request.args.get('lastname')
    if fname is None or lname is None:
        return jsonify(
          error="null in request or unknown parameters"
        ), 400
    if request.method == 'POST':
        if request.json:
            fname=request.json['firstname']
            lname=request.json['lastname']
        else:
            fname=request.form.get('firstname')
            lname=request.form.get('lastname')
    write_user(fname,lname)
    return jsonify(firstname=fname,lastname=lname)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
