from fastapi import FastAPI
import random
from typing import Dict

app = FastAPI()

orders = [random.randint(1, 100) for _ in range(5)]

@app.get("/api/getOrders")
def get_order() -> Dict[str, list]:
    if bool(random.getrandbits(1)):
        del orders[0]
    else:
        orders.append(orders[-1] + 1)
    return { "orders": orders }
