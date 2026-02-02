import json
import random
import time
import boto3
from datetime import datetime

# -------- CONFIG --------
BUCKET = "de-project-raw-sales-aritra"
BASE_PREFIX = "sales"
REGION = "us-east-1"

MAX_RECORDS = 100        # flush after 100 events
MAX_INTERVAL = 60        # or every 60 seconds

# ------------------------

s3 = boto3.client("s3", region_name=REGION)

users = list(range(1000, 1100))
products = list(range(200, 250))
payment_types = ["UPI", "Credit Card", "Debit Card", "Net Banking", "Wallet"]

order_id = 1
buffer = []
last_flush_time = time.time()


def generate_sale():
    global order_id

    quantity = random.randint(1, 5)
    unit_price = round(random.uniform(100, 5000), 2)

    sale = {
        "order_id": order_id,
        "user_id": random.choice(users),
        "product_id": random.choice(products),
        "quantity": quantity,
        "unit_price": unit_price,
        "total_amount": round(quantity * unit_price, 2),
        "payment_type": random.choice(payment_types),
        "order_time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }

    order_id += 1
    return sale


def flush_to_s3(records):
    if not records:
        return

    now = datetime.utcnow()
    date_str = now.strftime("%Y-%m-%d")
    ts = int(time.time())

    key = f"{BASE_PREFIX}/date={date_str}/sales_{ts}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body="\n".join(json.dumps(r) for r in records)
    )

    print(f"Flushed {len(records)} records to s3://{BUCKET}/{key}")


print("🚀 Starting Sales Generator (micro-batch mode)...")

while True:
    buffer.append(generate_sale())

    now = time.time()

    if len(buffer) >= MAX_RECORDS or (now - last_flush_time) >= MAX_INTERVAL:
        flush_to_s3(buffer)
        buffer.clear()
        last_flush_time = now

    time.sleep(1)
