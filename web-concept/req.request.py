# import request to get the url request
import requests


r = requests.get("https://google.com")
print("Status:",r.status_code)

