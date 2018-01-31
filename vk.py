from urllib.parse import urlencode

from pip._vendor import requests

AUTH_URL = "https://oauth.vk.com/authorize"
APP_ID = 6354145

auth_data = {
    "clent_id": APP_ID,
    "display": "mobile",  #popup, mobile
    "scope": "friends",  #friends, video
    "response_type": "token",
    "v": "5.71",
}

#print ("?".join((AUTH_URL, urlencode(auth_data))))

TOKEN = ""

params = {
    "access_token": TOKEN
}
#response = requests.get("https://api.vk.com/method/friends.getOnline",params)
#print (response.json())
#print (type(response.json()))
#print (response.json()['response'])

#response = requests.get ("https://api.vk.com/method/status.get",params)
#print("#1 get:", response.json())

#params["text"] = "some new status"

#response = requests.get ("https://api.vk.com/method/status.set",params)
#print("set", response.json())

#response = requests.get ("https://api.vk.com/method/status.get",params)
#print("#2 get:", response.json())

response = requests.get("https://api.vk.com/method/friends.getMutual",params)
source_uid = 2044169
target_uid = (6434915, 14211499)
print(response.json())

