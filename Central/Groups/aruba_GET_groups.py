import requests
from pprint import pprint as pp
import aruba_refresh_token
import yaml

base_url = 'https://apigw-uswest4.central.arubanetworks.com'
url = base_url + '/configuration/v2/groups?limit=20&offset=0'
print(url)
#Reading the auth.yaml document
with open('auth.yaml', 'r') as f:
    key_data = yaml.load(f, Loader=yaml.FullLoader)
    aruba_apikey = (key_data['access_token'])

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer' ' ' + aruba_apikey
}
# Script will run and see if the token is invalid or not.
# If invalid new token will be generated with the refresh key
# Updated data will be appended to auth.yaml
# If the token is valid then the data will be displayed
def check_token():
    x = 'invalid_token'
    response = requests.get(url, headers=headers)
    data = response.json()
    err_data = data.get('error',[])
    print(err_data)
    if x in err_data:
        print('~~~Refreshing Token~~~')
        aruba_refresh_token.ref_token()
        print('~~~Jump to next function~~~')
        check_data()
        print('~~~ Script was successful ~~~')
    else:
        pp(data)
        print ('~~~ Script was successful ~~~')

def check_data():
    with open('auth.yaml', 'r') as f:
        key_data = yaml.load(f, Loader=yaml.FullLoader)
        aruba_apikey = (key_data['access_token'])

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer' ' ' + aruba_apikey
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    pp(data)

if __name__ == "__main__":
         check_token()
         ### Disabled - For Testing only right now ####
         #check_data()
