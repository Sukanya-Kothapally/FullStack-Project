import config
import token_generator as token
import urllib.request
import ast

authKey = token.token_gen()
symptoms_dict = {'Name': [], 'ID': []}  # stores the name and id which will be passed on to the frontend
symptoms = {}   # dictionary that will store the data as name:id
symptoms_name = []   # This list of all sorted symptom names
ids = []

def fetch_symptoms():
    url = config.priaid_health_url + '/symptoms?token=' + authKey + '&format=json&language=en-gb'
    results_symptoms = urllib.request.urlopen(url).read()
    json_symptoms = ast.literal_eval(results_symptoms.decode("utf-8"))    # converting the byte string to string type

    for symptom in json_symptoms:
        ID = symptom['ID']
        Name = symptom['Name'].lower()  # converting to lower case to avoid Case-mismatch
        ids.append(ID)
        global symptoms_name
        symptoms_name.append(Name)
        symptoms[Name] = ID

    symptoms_dict['Name'] = symptoms_name
    symptoms_dict['ID'] = ids
    symptoms_name = sorted(symptoms_name, key=len, reverse=True)
    return symptoms

