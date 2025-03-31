import requests
url = "http://localhost:3000/posts/4"
data = {
        "views" : 800
}
respose = requests.patch(url,json= data)
print(respose.status_code)
print(respose.json())