import requests

url = 'http://127.0.0.1:5000/dados'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Received data: ', data)
else:
    print('Error! The monster data could not be fetched :(', response.status_code)

