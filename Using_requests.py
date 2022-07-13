import requests
import json


API_KEY = ''
# API_SECRET = ''

BASE_URL = "https://fapi.binance.com"

url = BASE_URL + "/fapi/v1/klines"

parameters = {
	"symbol":"ETHBUSD",
	"intervel":"4h",
	"limit":2
}

response = requests.get(url, params=parameters)

print(response.text)