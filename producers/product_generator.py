import json
import random
import boto3
import os

BUCKET = "de-project-raw-sales-aritra"
PREFIX = "products"
REGION = "us-east-1"

s3 = boto3.client(
    "s3",
    region_name=REGION,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

product_names = [
    "Laptop", "Smartphone", "Headphones", "Tablet",
    "Smartwatch", "Camera", "Printer", "Monitor",
    "Keyboard", "Mouse"
]

categories = ["Electronics", "Accessories", "Computing", "Gadgets"]

product_id_start = 200
num_products = 50

products = []

for i in range(num_products):
    products.append({
        "product_id": product_id_start + i,
        "product_name": f"{random.choice(product_names)}-Model-{i}",
        "category": random.choice(categories),
        "current_price": round(random.uniform(500, 5000), 2)
    })

print("📦 Uploading Products to S3...\n")

for product in products:
    key = f"{PREFIX}/category={product['category']}/product_{product['product_id']}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(product)
    )

    print("Uploaded:", product)
