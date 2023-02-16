import requests
from getpass import getpass

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'secret'
with open('reddit_api_personal_use_script.txt', 'r') as fp:
    client_id = fp.readlines()[0]

with open ('reddit_api_secret.txt', 'r') as fp:
    secret_token = fp.readlines()[0]

print(client_id)
print(secret_token)

auth = requests.auth.HTTPBasicAuth(client_id, secret_token)

password = getpass()
# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'El_Pasta',
        'password': password}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'andebraa_test_api/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

print(res)
# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
