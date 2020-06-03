import json
from flask import Flask, render_template, request
from flask import render_template,make_response
from flask import Flask, request, redirect, url_for
import googlemaps
import get_symptoms as get_sym
import recreation as rec
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/live+/symptom-checker')
def two():
    symptoms = get_sym.fetch_symptoms()
    return render_template("symptom-checker.html", symptoms=symptoms)



@app.route('/live+/recreation/', methods=['POST','GET'])
def locationforparks():
        return render_template("recreationform.html")

@app.route("/live+/recreationdata/",methods=['POST','GET'])
def parks_data():
        recDict=rec.fetch()
        locationfromhtml=rec.locationfunction()
        if(recDict=="No Location given, Please give a cityname!"):
            return render_template("recreationform.html", recDict=recDict)
        else:
            Dictstr=json.dumps(recDict)
            resultsdata=json.loads(Dictstr)
            return render_template("recreation.html", resultsdata=resultsdata,locationfromhtml=locationfromhtml)

if __name__ == '__main__':
    app.run(debug=True)