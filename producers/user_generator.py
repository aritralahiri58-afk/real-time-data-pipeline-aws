import json
import random

names = [
    "Amit", "Rahul", "Priya", "Sneha", "Arjun", "Kavya",
    "Rohan", "Meera", "Vikram", "Ananya"
]


cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad",
    "Chennai", "Kolkata", "Pune", "Ahmedabad"
]


users = []

user_id_start = 1000
num_users = 100

for i in range(num_users):
    user = {
        "user_id": user_id_start+1,
        "name": random.choice(names),
        "phone_number": f"+91{random.randint(7000000000, 9999999999)}",
        "city": random.choice(cities)
    }
    users.append(user)

print("Generating User Dimension Data....\n")

for u in user:
    print(json.dumps(u))

