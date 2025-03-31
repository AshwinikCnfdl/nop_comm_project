import requests
url = "http://localhost:3000/posts"
data = {
       'id': '4',
        'title' : "the java",
        'views' : 500
}
respose = requests.post(url,json= data)
print(respose.status_code)
print(respose.json())