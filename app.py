# Andrew Stade
# 1/29/2021
# afs18c
# The program in this file is the individual work of Andrew Stade.

from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/add')
def new_review():
   return render_template('addReview.html')
   
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         un = request.form['Username']
         rt = request.form['Restaurant']
         fd = request.form['Food']
         sv = request.form['Service']
         amb = request.form['Ambience']
         pce = request.form['Price']
         ovr = request.form['Overall']
         rev = request.form['Review']
         
         with sql.connect("reviewData.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO reviews (Username,Restaurant,Food,Service,Ambience,Price,Overall,Review) VALUES (?,?,?,?,?,?,?,?)",(un,rt,fd,sv,amb,pce,ovr,rev) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("index.html",msg = msg)
         con.close()   

@app.route('/get')
def new_get():
   return render_template('getReviews.html')

@app.route('/find',methods = ['POST', 'GET'])
def find():
    if request.method == 'POST':
      try:
         rows = []
         search = request.form['Restaurant']
         msg = search
         with sql.connect("reviewData.db") as con:
            con.row_factory = sql.Row
            
            cur = con.cursor()
            cur.execute("SELECT * FROM reviews WHERE Restaurant LIKE '%'")
            rows = cur.fetchall()
      finally:
         return render_template("showReviews.html",rows = rows,msg = msg)

@app.route('/top')
def new_top():
   con = sql.connect("reviewData.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("SELECT * FROM reviews ORDER BY Overall DESC")
   
   rows = cur.fetchmany(10)
   return render_template("showReport.html",rows = rows)
   
if __name__ == '__main__':
   app.run(debug = True)         