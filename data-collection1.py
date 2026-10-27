import json

data = '''
[
    {
        "product": "Laptop",
        "price": 1200
    },
    {
        "product": "PC",
        "price": 2400
    }
]
'''

result = json.loads(data)

for item in result:
  print(item["product"])
  print(item["price"])
