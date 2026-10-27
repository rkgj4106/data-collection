import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://localhost:30102/index.html"

response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(
    response.text,
    "html.parser"
)
products = soup.find_all(
    "div",
    class_="product"
)
product_names = []

for product in products:
    product_names.append(product.text.strip())

df = pd.DataFrame({
    "product": product_names
})

df.to_csv(
    "products.csv",
   # index=False,
    encoding="utf-8-sig"
)

