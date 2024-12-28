from django.test import TestCase

# Create your tests here.
import requests
import json

URL = 'http://127.0.0.1:8000/stuapi/'
def add_data():
    data = {
        'name':'Rajesh',
        'roll': '103',
        'city' : 'Patna'
    }
    json_data= json.dumps(data)
    r = requests.post(url=URL, data = json_data)
    result =r.json()
    print (result)
#add_data()

def get_data():
    URL = 'http://127.0.0.1:8000/stuapi/'
    r = requests.get(url=URL)
    result =r.json()
    print (result)
get_data()

def update_data():
    data = {
        'id':3,
        'city' : 'Nalanda Bihar India'
    }
    json_data= json.dumps(data)
    r = requests.put(url=URL, data = json_data)
    try:
        result =r.json()
        print (result)
    except Exception as e:
        print ("e",e,r)
#update_data()

def delete_data():
   data = {
    'id':5
    }
   json_data = json.dumps(data)
   r = requests.delete(url= URL , data = json_data)
   data = r.json()
   print(data)

delete_data()