from flask import Flask, render_template,request,flash,redirect,url_for
import sqlite3
import folium
from folium.plugins import MarkerCluster

app = Flask(__name__)
app.secret_key="S3CR3T K3Y"

con=sqlite3.connect("database.db")
con.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, Vin INTEGER ,LicencePlate TEXT,Driver TEXT,MMYyear INTEGER,MMYmake TEXT, MMYmodel TEXT, CustomerName TEXT, Office TEXT, StatusIgnition TEXT, StatusSpeed INTEGER, LocationLat REAL, LocationLon REAL)")
#con.execute("INSERT INTO data (Vin,LicencePlate, Driver,MMYyear,MMYmake,MMYmodel,CustomerName,Office,StatusIgnition,StatusSpeed,LocationLat,LocationLon) VALUES (3278898,	'72-5832419',	'Janeen',	1984,	'Suzuki',	'SJ 410',	'Edithe',	'Zoomdog',	'OFF'	,85,	20.9110916,	52.1584604		)");
con.commit()

m = folium.Map(location=[20.5937, 78.9629], zoom_start=6)
tooltip = 'Click For More Info'

@app.route('/')
def map():
    con=sqlite3.connect("database.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM data")
    data=cur.fetchall()
    print(data)
    marker_cluster = MarkerCluster().add_to(m)
    for row in data:
        lat = row[11]
        lon = row[12]
        html = '<strong>Name :' + str(row[3]) + '<br> VIN :' + str(row[1]) + ' <br> Speed :' + str(row[10])+' mph </strong>'
        iframe = folium.IFrame(html)
        popup = folium.Popup(iframe,min_width=150,max_width=150)
        
        folium.Marker(location = [lat, lon], popup = popup, tooltip=tooltip).add_to(marker_cluster)
        m.save(outfile='C:/Users/bhawn/Project_Motorq/templates/map.html')
    return render_template('index.html')

 
 
if __name__ == "__main__":
    app.run(debug=True)