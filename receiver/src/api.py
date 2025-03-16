from fastapi import FastAPI, Header, HTTPException, Request
from typing import Annotated
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


@app.get("/api/orders")
def get_order() -> list[Order]:
    return order_store.get_orders()


@app.post("/api/orders/webhook")
async def add_order_webhook(
    order: OrderRequest,
    request: Request,
    x_signature: Annotated[str | None, Header()] = None,
):
    if not x_signature:
        raise HTTPException(status_code=400, detail="X-Signature header required")
    if not webhook_verifier.signature_valid(await request.body(), x_signature):
        raise HTTPException(status_code=400, detail="Invalid signature")

    order_store.add_order(order.orderNumber, order.timeoutSeconds)
