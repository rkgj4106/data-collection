import requests
import pandas as pd

url = "http://localhost:30102/books"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

print(df)
