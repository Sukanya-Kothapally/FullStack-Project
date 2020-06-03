from flask import request
import googlemaps

def fetch():
    googleMaps = googlemaps.Client(key='AIzaSyAQO23hWoMorbHodnChbFZ42g-BiGEcSqM')
    location = request.form["location"]
    if (location != ""):
        geography_result = googleMaps.geocode(location)
        latlng = [(float(d['geometry']['location']['lat']), float(d['geometry']['location']['lng'])) for d in geography_result]
        info = googleMaps.places(query="hospitals", location=latlng[0],radius='100')
        hospitalList = info["results"]
        finaloutput = [[str(r['name']), str(r['formatted_address']), str(r['rating'])] for r in hospitalList]
        # print(finalresult)
        return finaloutput
    else:
        return "No Location given, Please give a place!!!";
def locationfunction():
    googleMaps = googlemaps.Client(key='AIzaSyAQO23hWoMorbHodnChbFZ42g-BiGEcSqM')
    location = request.form["location"]
    return location