# -*- coding: utf-8 -*-

from flask import Flask, render_template,request,flash,redirect,url_for
import sqlite3

app = Flask(__name__)
app.secret_key="123"

con=sqlite3.connect("database.db")
con.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, Vin INTEGER ,LicencePlate TEXT,Driver TEXT,MMYyear INTEGER,MMYmake TEXT, MMYmodel TEXT, CustomerName TEXT, Office TEXT, StatusIgnition TEXT, StatusSpeed INTEGER, LocationLat REAL, LocationLon REAL)")
#con.execute("INSERT INTO data(Vin,LicencePlate, Driver,MMYyear,MMYmake,MMYmodel,CustomerName,Office,StatusIgnition,StatusSpeed,LocationLat,LocationLon) VALUES (3278898,	'72-5832419',	'Janeen',	1984,	'Suzuki',	'SJ 410',	'Edithe',	'Zoomdog',	'OFF'	,85,	20.9110916,	52.1584604)");
con.close()

@app.route('/')
def Index():
    con=sqlite3.connect("database.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM data")
    data=cur.fetchall()
    con.close()
    return render_template("index.html",vehicles=data)

#this route is for inserting data to database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method=='POST':
        try:
            Vin=request.form['Vin']
            LicencePlate=request.form['LicencePlate']
            Driver=request.form['Driver']
            MMYyear=request.form['MMYyear']
            MMYmake=request.form['MMYmake']
            MMYmodel=request.form['MMYmodel']
            CustomerName=request.form['CustomerName']
            Office=request.form['Office']
            StatusIgnition=request.form['StatusIgnition']
            StatusSpeed=request.form['StatusSpeed']
            LocationLat=request.form['LocationLat']
            LocationLon=request.form['LocationLon']
            con=sqlite3.connect("database.db")
            cur=con.cursor()
            cur.execute("INSERT INTO data(Vin,LicencePlate, Driver,MMYyear,MMYmake,MMYmodel,CustomerName,Office,StatusIgnition,StatusSpeed,LocationLat,LocationLon) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(Vin,LicencePlate, Driver,MMYyear,MMYmake,MMYmodel, CustomerName,Office,StatusIgnition,StatusSpeed,LocationLat,LocationLon))
            con.commit()
            flash("Record Added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("Index"))
            con.close() 

#this is our update route where we are going to update our employee
@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
 
    con=sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM data where id=?",(id))
    data = cur.fetchone()
    con.close()

    if request.method=='POST':
        try:
            LicencePlate=request.form['LicencePlate']
            Driver=request.form['Driver']
            Office=request.form['Office']
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            cur.execute("UPDATE data SET LicencePlate=?,Driver=?,Office=? where id=?",(LicencePlate,Driver,Office,id))
            con.commit()
            flash("Update Successfully","success")
        except:
            flash("Error in Update Operation","danger")
        finally:
            return redirect(url_for("Index"))
            con.close()
            
#This route is for deleting our vehicles
@app.route('/delete/<string:id>/', methods = ['GET', 'POST'])
def delete(id):
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where id=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for('Index'))
        con.close()
        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)