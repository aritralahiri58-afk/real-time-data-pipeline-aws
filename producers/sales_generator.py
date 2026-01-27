import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

#Creating Kafka Producer
#We serialize events into JSON and encode them as UTF-8 bytes before sending to Kafka, since Kafka producers work with byte arrays
producer=KafkaProducer(
        bootstrap_servers='127.0.0.1:9092',
        api_version=(0, 10, 1),
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
#Mock Sales data pools
users = list(range(1000, 1100))
products = list(range(200,250))
payment_type =  ["UPI", "Credit Card", "Debit Card", "Net Banking", "Wallet"]

order_id=1

def generate_sale():
    global order_id

    unit_price = round(random.uniform(100,5000),2)
    quantity = random.randint(1,5)
    sale = {
        "order_id": order_id,
        "user_id": random.choice(products),
        "product_id": random.choice(products),
        "quantity": quantity,
        "unit_price": unit_price,
        "total_amount": round(unit_price * quantity, 2),
        "payment_type": random.choice(payment_type),
        "order_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    order_id+=1
    return sale

#MAIN FUNCTION
if __name__=="__main__":
    print("Starting Sales Fact Generator....\n")

    while True:
        sale_event = generate_sale()
        producer.send("sales_topic",sale_event)
        print(json.dumps(sale_event))
        time.sleep(10)