import requests

url = 'http://127.0.0.1:5000/worker'  # Your Flask API URL

data = {
    'name': 'Alice',
    'status': 'On the way',
    'location': 'Street 1, City A'
}

response = requests.post(url, json=data)

print(response.json())
