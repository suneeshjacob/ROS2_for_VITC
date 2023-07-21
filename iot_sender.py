import requests
import json
import time

url = 'https://8863-49-37-148-1.ngrok.io/'
headers = {'Content-Type':'application/json'}
data = lambda number: {'data' : 'Hello World: {number}'}

for i in range(100):
	json_data = json.dumps(data(i+1))
	r = requests.post(url, headers = headers, data = json_data)
	time.sleep(1)
