# import request to get the url request
import requests

r = requests.get("https://google.com")
print("Status:", r.status_code)

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)
