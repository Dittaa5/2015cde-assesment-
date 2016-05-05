from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)
import os


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/miketyson")
def miketyson():
    return render_template("miketyson.html")
    

    
@app.route("/amirkhan")
def amirkhan():
    return render_template("amirkhan.html")

@app.route("/mannypac")
def mannypac():
    return render_template("mannypac.html")

@app.route("/xtrainers")
def xtrainers():
    return render_template("xtrainers.html")
    
@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("databsae.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("databsae.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)
   
if __name__ == '__main__':
    app.debug = True
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)