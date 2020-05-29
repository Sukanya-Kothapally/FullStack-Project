import json
from flask import Flask, render_template, request
import get_symptoms as get_sym
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/medical_conditions/')
def two():
    symptoms = get_sym.fetch_symptoms()
    return render_template("medical_conditions.html", symptoms=symptoms)

if __name__ == '__main__':
    app.run(debug=True)