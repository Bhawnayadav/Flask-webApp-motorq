# Flask-webApp-motorq
 
###Table of Content
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
location points from the vehicles data to render on the map using GET request.
  - API : GET /vehicles
    + Features of landing page:
    + There should be a marker cluster indicating the vehicles on the map.
    + On zooming in, the clusters should split into individual vehicle
  markers
    + On hovering over the markers, popup should be visible containing the vehicle
  info.
    + There should be a link to vehicle management page from the dashboard.


