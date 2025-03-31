import requests

url = "http://localhost:3000/comments/2"
respose = requests.get(url)
print(respose.status_code)
print(respose.json())

# grid selenium