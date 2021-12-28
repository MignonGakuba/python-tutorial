# import request to get the url request
import requests

r = requests.get("https://google.com")
print("Status:", r.status_code)


f = open("./page.html", "w+", encoding="utf-8")
f.write(r.text)



# creat a send to creat http reuqest