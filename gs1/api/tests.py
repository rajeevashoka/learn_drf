from django.test import TestCase

# Create your tests here.
import requests
URL= 'http://127.0.0.1:8000/stuinfo/'
r = requests.get(url=URL)
print (r)
data = r.json()
print (data)
