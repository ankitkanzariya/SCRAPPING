import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}

url = "https://www.amazon.in/s?k=iphone"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

for item in soup.select('.a-size-medium.a-color-base.a-text-normal'):
    print("TITLE:", item.get_text(strip=True))

for price in soup.select('.a-price-whole'):
    print("Price:", price.get_text(strip=True))