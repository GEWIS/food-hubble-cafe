from fastapi import FastAPI
import random
from typing import Dict
from datetime import datetime

app = FastAPI()

orders = [{
    "number": 123,
    "timeoutSeconds": 10,
    "startTime": datetime.now()
}]

@app.get("/api/getOrders")
def get_order():
#     if len(orders) > 1 and bool(random.getrandbits(1)):
#         del orders[0]
#     else:
    orders.append({
        "number": orders[-1]["number"] + 1,
        "timeoutSeconds": 10,
        "startTime": datetime.now()
    })
    return orders