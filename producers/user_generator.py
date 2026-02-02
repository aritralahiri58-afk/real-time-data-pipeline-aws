import json
import random
import boto3
import os

BUCKET = "de-project-raw-sales-aritra"
PREFIX = "users"
REGION = "us-east-1"

s3 = boto3.client(
    "s3",
    region_name=REGION,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

names = ["Amit", "Rahul", "Priya", "Sneha", "Arjun", "Kavya",
         "Rohan", "Meera", "Vikram", "Ananya"]

cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad",
          "Chennai", "Kolkata", "Pune", "Ahmedabad"]

users = []

user_id_start = 1000
num_users = 100

for i in range(num_users):
    users.append({
        "user_id": user_id_start + i,
        "name": random.choice(names),
        "phone_number": f"+91{random.randint(7000000000, 9999999999)}",
        "city": random.choice(cities)
    })

print("📦 Uploading Users to S3...\n")

for user in users:
    key = f"{PREFIX}/city={user['city']}/user_{user['user_id']}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(user)
    )

    print("Uploaded:", user)
