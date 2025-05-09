import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts")
print("status code is",r)

data = r.json()

for item in data:
    print(f"ID: {item['id']}, TITLE: {item['title']}")