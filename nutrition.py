import spoonacular as sp
from flask import request
api = sp.API("356a7bee2cc2417b9b37ea217d35247b")


def nutrition():
    dish = request.form["dishname"]
    # print(dish)
    # dish = input
    response = api.guess_nutrition_by_dish_name(dish)
    data = response.json()
    # res = ["data['calories']['value']", "data['protein']['value']", "data['carbs']['value']"]
    res = []
    res1 = data['calories']['value']
    res2 = data['protein']['value']
    res3 = data['carbs']['value']
    res4 = data['fat']['value']
    res.append(res1)
    res.append(res2)
    res.append(res3)
    res.append(res4)

    return res

def food_jokes():
    api = sp.API("356a7bee2cc2417b9b37ea217d35247b")
    response = api.get_a_random_food_joke()
    data = response.json()
    return data['text']
#
# food_jokes()