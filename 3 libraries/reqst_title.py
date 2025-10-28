import requests

URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(URL)
print(response)

posts = response.json()
print(posts)

for i, post in enumerate(posts[:5], start=1):  # first 5
        print(f"{i}. {post.get('title')}")