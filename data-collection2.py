import pandas as pd

data = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 25},
    {"product": "Keyboard", "price": 50}
]

df = pd.DataFrame(data)

print(df)