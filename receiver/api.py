from fastapi import FastAPI, Header, HTTPException
from typing import Dict, Annotated
from pydantic import BaseModel
from typing_extensions import TypedDict

from webhook import WebhookVerifier
from orders import OrderStore, Order

app = FastAPI()
webhook_verifier = WebhookVerifier()
order_store = OrderStore()

class OrderRequest(BaseModel):
    orderNumber: int
    timeoutSeconds: int | None = None

class OrderResponse(TypedDict):
    orders: list[Order]

@app.get("/api/getOrders")
def get_order() -> OrderResponse:
    return {
        "orders": order_store.get_orders()
    }

@app.post("/api/order/webhook")
def add_order_webhook(order: OrderRequest, x_signature: Annotated[str | None, Header()] = None):
    if not x_signature or not webhook_verifier.signature_valid(order.model_dump_json(), x_signature):
        raise HTTPException(status_code=400, detail="Invalid signature")

    order_store.add_order(order.orderNumber, order.timeoutSeconds)

# TODO: remove this after testing
@app.post("/api/order")
def add_order(order: OrderRequest):
    order_store.add_order(order.orderNumber, order.timeoutSeconds)
