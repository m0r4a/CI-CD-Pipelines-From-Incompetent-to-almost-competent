import requests
import json

url = "http://localhost:8088/greet"

payload = {"name": "Mora"}

try:
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        greet = data.get("greet")

        print(f"Response from the Go server: {greet}")
    else:
        print(f"Error, the Go server replied with the code {response.status_code}")
        print(response.text)

except requests.exceptions.ConnectionError as e:
    print("Couldn't connect with the Go server")
    print("Is server.go running?")    
