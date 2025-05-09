import  requests

# Get request
response = requests.get("https://httpbin.org/get")
print(response.text)
print(response.status_code)
print(response.json)

# POST request
data = {'key1': 'value1'}
response = requests.post("https://httpbin.org/get", data=data)
print(response.status_code)

import time
print(time.time())