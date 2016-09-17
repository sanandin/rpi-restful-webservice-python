from __future__ import print_function
from flask import Flask, render_template, request
import sqlite3 as sql
import json
from flask import Response
app = Flask(__name__)

@app.route('/')
def features():
   return render_template('index.html')

@app.route('/enternew')
def new_student():
   return render_template('employee.html')

@app.route('/update')
def update_student():
   return render_template('update.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         age = request.form['age']
         eid = request.form['eid']
         designation = request.form['designation']
         with sql.connect("/tmp/employeeschema.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO employee (age,name,empId,designation) VALUES (?,?,?,?)",(age,nm,eid,designation) )
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "Error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("/tmp/employeeschema.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from employee")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

@app.route('/upd',methods = ['POST', 'GET'])
def upd():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         upd_nm = request.form['upd_nm']
    
         with sql.connect("/tmp/employeeschema.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE employee set name=? where name=?", (upd_nm,nm))
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "Error in update operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/cpuinfo')
def cpu_info():
   line_list={}
   with open('/proc/cpuinfo', 'r') as f:
      for line in f:
         if (line.rstrip("\n").split(":")[0] != "" and line.rstrip("\n").split(":")[1] != ""):
            key = line.rstrip("\n").split(":")[0]
            value = line.rstrip("\n").split(":")[1]
            line_list.update({key:value})
   return render_template('display_cpuinfo.html',result=line_list)

if __name__ == '__main__':
   app.run('0.0.0.0',debug = True)
