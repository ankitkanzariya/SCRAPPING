import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all("span", class_="text")
for quote in quotes:
    print("QUOTE:", quote.text)

