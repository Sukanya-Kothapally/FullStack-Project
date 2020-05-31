import json
from flask import Flask, render_template, request
from flask import render_template,make_response, jsonify
from flask import Flask, request, redirect, url_for
import hospitals as hs

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
    hosDict = hs.fetch()
    locationfromhtml = hs.locationfunction()
    if (hosDict == "No Location given, Please give a place!!!"):
        return render_template("locationform.html", res=hosDict)
    else:
        Dictstr = json.dumps(hosDict)
        resultsdata = json.loads(Dictstr)
        return render_template("hospitalsList.html", res=resultsdata, locationfromhtml=locationfromhtml)







if __name__ == '__main__':
    app.run(debug=True)