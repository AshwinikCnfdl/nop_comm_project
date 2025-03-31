import requests
url = "http://localhost:3000/posts/4"
data = {
       'id': '4',
        'title' : "the java programming",
        'views' : 500
}
respose = requests.put(url,json= data)
print(respose.status_code)
print(respose.json())