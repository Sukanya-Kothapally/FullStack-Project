import token_generator as token
import ast
import config
import urllib.request

authKey = token.token_gen()


def api_symptom_result(symptoms_ids, gender, year_of_birth):
    urlMedicalCondition = config.priaid_health_url + "/diagnosis?symptoms=[" + symptoms_ids + "]&gender=" + gender + "&year_of_birth=" + year_of_birth + "&token=" + authKey + "&format=json&language=en-gb"
    resultsMC = urllib.request.urlopen(urlMedicalCondition).read()  # returns a byte string
    api_results = ast.literal_eval(resultsMC.decode("utf-8"))  # converting the byte string to string and then parsing it into a list
    api_results_dict = {}
    for issue in api_results:
        accuracy=issue['Issue']['Accuracy']
        api_results_dict[accuracy] = issue['Issue']['Name']

    return api_results_dict
