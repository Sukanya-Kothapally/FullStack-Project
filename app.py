import json
from flask import Flask, render_template, request
from flask import render_template,make_response
from flask import Flask, request, redirect, url_for

import googlemaps

app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template("index.html")

#button2 home page
@app.route('/live+/location/', methods=['POST','GET'])
def enterLocation():
        return render_template("locationform.html")

#button2 resultspage
@app.route("/live+/hospitalsresult/",methods=['POST','GET'])
def locationHospital():
        googleMaps = googlemaps.Client(key='AIzaSyAQO23hWoMorbHodnChbFZ42g-BiGEcSqM') #connecting to google
        location = request.form["location"]  # getting address entered by user in form
        geocoding_result = googleMaps.geocode(location)

        locationLatLng=[(float(i['geometry']['location']['lat']), float(i['geometry']['location']['lng'])) for i in geocoding_result] #extracting latitude and longitude using the address enetered by user
        result=googleMaps.places(query="hospital", location=locationLatLng[0], radius = '100')['results'] #getting the name of hospitals near the address entered by user

        hospitalResult=[[str(r['name']),str(r['formatted_address']),str(r['user_ratings_total']), str(r['rating'])] for r in result]
        return render_template("hospitalsList.html", res=hospitalResult)


if __name__ == '__main__':
    app.run(debug=True)