import requests
import json

# get request from webpage
response = requests.get("https://api.stackexchange.com/2.2/answers?order=desc&sort=activity&site=stackoverflow")
print(response.json())

for data in response.json()["items"]:
    count = 0
    if data["owner"] != "":
        # type of data is dictionary so data[key] = value
        print("Name: {0} \nID: {1}".format(data["owner"]["display_name"],data["owner"]["user_id"]))
        count+=1

    print()