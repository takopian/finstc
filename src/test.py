import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "car/1")
# response = requests.patch(BASE + "video/2", {})
print(response.json())

response = requests.get(BASE + "dealer/1")
print(response.json())

response = requests.post(BASE + "dealer/add", {'name': 'opa'})
print(response.json())

response = requests.patch(BASE + "dealer/2", {'name': 'rrr'})
print(response.json())

response = requests.post(BASE + "car/add", {'name': 'cheburek'})
print(response.json())

response = requests.post(BASE + "car/add", {'name': 'lada'})
print(response.json())

response = requests.delete(BASE + "car/3")
print(response.json())

response = requests.post(BASE + "dealer/1/car/2", {'quantity': 153, 'price': 33})
print(response.json())

response = requests.post(BASE + "dealer/2/car/1", {'quantity': 1, 'price': 70000})
print(response.json())

response = requests.post(BASE + "dealer/2/car/2", {'quantity': 156, 'price': 7099000})
print(response.json())

response = requests.get(BASE + "dealer/2/car/2")
print(response.json())

response = requests.get(BASE + "dealer/1")
print(response.json())
