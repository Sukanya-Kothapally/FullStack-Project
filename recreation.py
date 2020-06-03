from flask import request
import googlemaps

def fetch():
    googleMaps = googlemaps.Client(key='AIzaSyAQO23hWoMorbHodnChbFZ42g-BiGEcSqM')
    location = request.form["location"]

    if (location != ""):
        geography_result = googleMaps.geocode(location)
        latlng = [(float(d['geometry']['location']['lat']), float(d['geometry']['location']['lng'])) for d in geography_result]
        info = googleMaps.places(query="trails", location=latlng[0],radius='100')
        recreationresult = info["results"]
        print(recreationresult)
        finalresult = [[str(res['name']), str(res['formatted_address']), str(res['rating'])] for res in recreationresult]
        # print(finalresult)
        return finalresult
    else:
        return "No Location given, Please give a cityname!";
def locationfunction():
    googleMaps = googlemaps.Client(key='AIzaSyAQO23hWoMorbHodnChbFZ42g-BiGEcSqM')
    location = request.form["location"]
    return location