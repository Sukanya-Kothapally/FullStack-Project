import spoonacular as sp
from flask import request
from ast import literal_eval

api = sp.API("356a7bee2cc2417b9b37ea217d35247b")

def mealPlan():
    diet_name = request.form['diet']

    options = request.form['exclude']

    calories_input = request.form['calories']
    list = options.split(",")
    li= []
    for i in list:
        li.append(str(i))

    response = api.generate_meal_plan(diet=diet_name, exclude=li, targetCalories=calories_input, timeFrame=None)
    data = response.json()
    items_data = data['items']



    x =[]
    for index in range (len(items_data)):
            # print(items_data[index]['day'], items_data[index]['slot'],literal_eval(items_data[index]['value'])['title'])
            x.append([items_data[index]['day'], items_data[index]['slot'],literal_eval(items_data[index]['value'])['title']])

    return x






