import token_generator as token
import ast
import config
import urllib.request

authKey = token.tokenGen()

def api_symptom_result(symptoms_ids, gender, year_of_birth):
    api_results_dict = {}
    get_symptoms_result = config.priaid_health_url + "/diagnosis?symptoms=[" + symptoms_ids + "]&gender=" + gender + "&year_of_birth=" + year_of_birth + "&token=" + authKey + "&format=json&language=en-gb"
    results = urllib.request.urlopen(get_symptoms_result).read()
    api_results = ast.literal_eval(results.decode("utf-8"))
    for result in api_results:
        accuracy = result['Issue']['Accuracy']
        api_results_dict[accuracy] = result['Issue']['Name']
    return api_results_dict
