from django.test import TestCase

# Create your tests here.
import requests
import json

URL = 'http://127.0.0.1:8000/stucreate/1'
data = {
    'name':'Rajeev',
    'roll': '101',
    'city' : 'Patna'
}
json_data= json.dumps(data)
print (type(json_data))
r = requests.post(url=URL, data = json_data)
result =r.json
print (result)