import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

#print(df.head())
df = df[
    [
        "id",
        "name",
        "email",
        "phone"
    ]
]
df.to_csv(
    "users.csv",
    index=False
)
