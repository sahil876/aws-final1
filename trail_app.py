from flask import Flask, render_template, request,flash,redirect,url_for
from flask import Response,send_file
from pymysql import connections
import os
import boto3
#from trial import * 

app = Flask(__name__)

import trial as db 

@app.route('/')
def index():
    
    return render_template('AddEmp1.html')

@app.route("/addemp",methods=['POST'])
def AddEmp():
	if request.method == 'POST':
		emp_id = request.form['emp_id']
		first_name=request.form['first_name']
		last_name = request.form['last_name']
		pri_skill = request.form['pri_skill']
		location = request.form['location']
		db.insert_details(emp_id,first_name,last_name,pri_skill,location)
		details = db.get_details()
		print(details)
		for detail in details:
			var = detail
		return render_template('AddEmp1.html',var=var)


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=80,debug=True)
