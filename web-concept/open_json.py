import os
import simplejson as json


file_data = open("ages.json","r+")
data = json.load(file_data)
print("Age is" , data["age"], "name is ", data["name"])