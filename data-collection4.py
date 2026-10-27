import requests
from bs4 import BeautifulSoup

url = "http://localhost:30102/index.html"

response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print(soup.title)

products = soup.find_all(
    "div",
    class_="product"
)

for product in products:
    print(product.text.strip())