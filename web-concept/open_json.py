import simplejson as json

# Read a json file with data and methode 'r+'
file_data = open("ages.json", "r+")
data = json.load(file_data)
print("Age is:", data["age"], "Name is :", data["name"])

# Create json file with data and methode 'w+'
create_json_file = open("data.json", "w+")
data = {"name": "Nick", "age": 27}
print("Created a new file with data")

create_json_file.write(json.dumps(data))
