import json
from flask import Flask,render_template,request,make_response, jsonify
from flask import redirect, url_for
import hospitals as hs
import nutrition as nt
import mealplan as mp
import googlemaps
import get_symptoms as get_sym
import symptoms_result as sym_res
import recreation as rec

app = Flask(__name__)


# home page
@app.route('/')
def index():
    return render_template("index.html")
  
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

@app.route('/live+/nutritionmealplan')
def selectOne():
    return render_template("nutritionmealplan.html")

@app.route('/live+/nutrition/', methods=['POST','GET'])
def giveDetails():
    return render_template("nutrition.html")

@app.route('/live+/nutrition/result', methods=['POST', 'GET'])
def giveResult():
    data = nt.nutrition()
    joke = nt.food_jokes()
    return render_template("nutritionResult.html", res=data, joke_result= joke)

@app.route('/live+/mealplan',methods=['POST', 'GET'])
def mealplan():
    return render_template("mealPlan.html")

@app.route('/live+/mealplan/result',methods=['POST', 'GET'])
def mealplanresult():
    data = mp.mealPlan()
    return render_template("mealPlanResults.html",res = data)

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

@app.route('/live+/symptom-checker')
def symptomChecker():
    symptoms = get_sym.fetch_symptoms()
    return render_template("symptom-checker.html", symptoms=symptoms)

@app.route('/live+/symptom-checker-result', methods=['POST'])
def symptomCheckerResult():
    data = request.get_json()
    fetch_api_result = sym_res.api_symptom_result(data["id"], data["gender"], data["year"])
    fetch_api_result_dict = json.dumps(fetch_api_result)
    return fetch_api_result_dict
  

if __name__ == '__main__':
    app.run(debug=True)