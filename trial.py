import pymysql
#import aws_credentials as rds
from pymysql import connections

conn = pymysql.connect(
        host= '', #endpoint of RDS
        port = 3306, #port number
        user = '', #database name 
        password = '',#database pass
        db = '',#database name
        )


#Table Creation
#cursor=conn.cursor()
#create_table=
#create table employee (emp_id varchar(20),first_name varchar(20),last_name varchar(20),pri_skill varchar(20),location varchar(20) )


#cursor.execute(create_table)


#insert query
def insert_details(emp_id,first_name,last_name,pri_skill,location):
    cur=conn.cursor()
    cur.execute("INSERT INTO employee(empid,fname,lname,pri_skill,location) VALUES (%s,%s,%s,%s,%s)",(emp_id,first_name,last_name,pri_skill,location))
    conn.commit()

#read the data
def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM employee")
    details = cur.fetchall()
    return details

