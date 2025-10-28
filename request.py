import requests
r = requests.get("https://github.com/ankitkanzariya")

print(r)

print(r.content)
print(r.encoding)
print(r.elapsed)
print(r.cookies)
print(r.history)
print(r.is_permanent_redirect)
print(r.is_redirect)

print(r.json)

print(r.url)
print(r.text)
print(r.request)

print(r.reason)

print(r.raise_for_status())
print(r.ok)