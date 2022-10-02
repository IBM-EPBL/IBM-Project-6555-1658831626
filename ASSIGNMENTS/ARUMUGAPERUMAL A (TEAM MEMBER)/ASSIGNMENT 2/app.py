from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         fname = request.form['fname']
         lname = request.form['lname']
         email = request.form['email']
         password = request.form['password']
         
         with sql.connect("users.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (fname,lname,email,password) VALUES (?,?,?,?)",(fname,lname,email,password) )
            con.commit()
            msg = "You have signed up successfully!"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("signup.html",msg = msg)
         con.close()

@app.route('/database')
def database():
   con = sql.connect("users.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from users")
   
   users = cur.fetchall();
   return render_template("database.html", users = users)


if __name__=='__main__':
    app.run(debug=True)

