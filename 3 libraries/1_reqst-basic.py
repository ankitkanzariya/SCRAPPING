import requests

# GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)   # 200 = success
print(response.json())        # JSON response (dict)
