import requests
import json

url = "https://api.example.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
