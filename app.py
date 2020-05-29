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
def location():
        return render_template("locationform.html")




if __name__ == '__main__':
    app.run(debug=True)