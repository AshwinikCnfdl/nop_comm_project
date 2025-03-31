import requests
url = "http://localhost:3000/posts/4"
respose = requests.delete(url)
print(respose.status_code)
print(respose.json())