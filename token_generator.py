import crendentials
import requests
import base64
import hmac
import json

# Generating token for APIMEDIC.
def tokenGen():
    username = crendentials.username
    password = crendentials.password
    authUrl = crendentials.priaid_auth_url

    HashString = hmac.new(bytes(password, encoding='utf-8'), authUrl.encode('utf-8')).digest()
    computedHashString = base64.b64encode(HashString).decode()

    bearer_credentials = username + ':' + computedHashString
    postHeaders = {
        'Authorization': 'Bearer {}'.format(bearer_credentials)
    }
    responsePost = requests.post(authUrl, headers=postHeaders)

    data = json.loads(responsePost.text)
    return data["Token"]
