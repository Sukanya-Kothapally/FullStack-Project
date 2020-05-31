import json
from flask import Flask, render_template
import recreation as rec


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/live+/recreation/', methods=['POST','GET'])
def location():
        return render_template("recreationform.html")

@app.route("/live+/recreationdata/",methods=['POST','GET'])
def map_doc():
        recDict=rec.fetch()
        locationfromhtml=rec.locationfunction()
        if(recDict=="No Location given, Please give a place!!!"):
            return render_template("recreationform.html", recDict=recDict)
        else:
            Dictstr=json.dumps(recDict)
            resultsdata=json.loads(Dictstr)
            return render_template("recreation.html", resultsdata=resultsdata,locationfromhtml=locationfromhtml)

if __name__ == '__main__':
    app.run(debug=True)