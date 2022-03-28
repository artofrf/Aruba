import requests
from pprint import pprint as pp
#### This script will referesh the token after 2 hours
import yaml

client_id = 'your-client-id'
client_secret = 'your-client-secret'
grant_type = 'refresh_token&'
expires_in = '30'
### There is a new refresh token each time token gets refreshed
refresh_token = 'your-refresh-token'
base_url = 'https://apigw-uswest4.central.arubanetworks.com'
### URL NOTES ###
### Domain Name: This is the domain name of the API gateway based on the location of the Aruba Central Customer account
### https://developer.arubanetworks.com/aruba-central/docs/api-oauth-access-token#section-requirements
### API Endpoint Path: Endpoint path is the path within the API Gateway domain.
### https://developer.arubanetworks.com/aruba-central/reference/apiget_idp_metadata

def ref_token():
    url = base_url + '/oauth2/token?client_id='+ client_id + 'client_secret='\
          + client_secret +'grant_type='+ grant_type +'refresh_token='+ refresh_token
    print(url)
    headers = {
      'Content-Type': 'application/json',
    }
    response = requests.post(url, headers=headers)
    data = response.json()
    print(data)
    #aruba_apikey = (data['access_token'])
    #aruba_refresh_token = (data['refresh_token'])
    #print(aruba_apikey)
    #print(aruba_refresh_token)
    #This will update the auth.yaml doc with the new keys
    with open('auth.yaml', 'w') as f:
        docs = yaml.dump(data,f)
        #documents = yaml.dump(aruba_apikey,f)

if __name__ == "__main__":
    ref_token()
