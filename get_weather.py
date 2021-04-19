import requests
from pprint import pprint

API_KEY = ''
city = input("Enter City Location: ")
result = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY)
pprint(result.json())
