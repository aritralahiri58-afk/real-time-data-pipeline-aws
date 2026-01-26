import json
import random

product_name = ["Laptop", "Smartphone", "Headphones", "Tablet", "Smartwatch",
    "Camera", "Printer", "Monitor", "Keyboard", "Mouse"]

Categories = ["Electronics", "Accessories", "Computing", "Gadgets"]

products = []

product_id_start = 200
num_products = 50

for i in range(num_products):
    product = {
        "product_id": product_id_start+1,
        "product_name": random.choice(product_name)+f"Model-{i}",
        "category": random.choice(Categories),
        "current_price": round(random.uniform(500, 5000),2)

    }
    product.append(product)

    print("Generating Product Dimension Data.....\n")

    for p in products:
        print(json.dumps(p))