# Flask-webApp-motorq
 
### Table of Content
* Introduction
* Prerequisites
* Installation Guide
* Supported Platforms

## 🗒️Introduction 

## Prerequisites✔️
Make sure you have 
* Python3
* Flask 
* pip3 
installed before proceeding with the further steps.

# ⚙️Installation
• Open cmd in your windows machine
• Navigate to the project directory you wish to have this project on.
• type $ pip3 install -r Requirements.txt
• clone or download the project in the directory from github ( Maintaining the project structure).
## Starting the project
• Navigate to Vehicle manaagement directory in cmd and type $python3 app.py ; this should run on localhost:5001
• Navigate to Map Application directory in cmd and type $python3 app.py ; this should run on localhost:5000
*Map application interacts with vehicle managemnt page using port 5001. 

## Result

### Map Application
location points from the vehicles data to render on the map using GET request.
  
    + Features of landing page:
    + A marker cluster indicating the vehicles on the map.
    + On zooming in, the clusters split into individual vehicle markers
    + On hovering over the markers, popups displays the vehicle info.
    + A link to vehicle management page from the page.

![MapClusterImage](/imags-Readme/Map_with_Clusters.png)

![Clusters seperated](/imags-Readme/Clusters_separated_into_individual_Markers.png)

![Vehicle Info](/imags-Readme/Vehicle_Info.png)

### Vehicle Management
Returns a list of vehicles and render on the vehicles page in tabular fashion and perform **CRUD** operations 
  + An edit button, where we can edit licensePlate, driver, office.
  + Supports infinite scrolling

![Vehicle Management](/imags-Readme/Vehicle_Management.png)

