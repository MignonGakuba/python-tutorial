# import request to get the url request
import requests

r = requests.get("https://bing.com")
print("Status:", r.status_code)


f = open("./page.html", "w+", encoding="utf-8")
f.write(r.text)



# Creat a send to creat http request with params
params = {"q":"pizza"}
r = requests.get("https://bing.com",params=params)

print("Status:", r.status_code)

print(r.url)
f = open("./page.html", "w+", encoding="utf-8")
f.write(r.text)

