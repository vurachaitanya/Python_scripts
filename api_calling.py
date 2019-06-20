import requests
import json

req = requests.get("https://jsonplaceholder.typicode.com/posts")
#print(req.text[{"userId"}])

if req.status_code == 200:
  test = (json.loads(req.content.decode('utf-8')))
  print(test[2]['id'])
else:
  print("None")
