from datetime import datetime, timedelta
from typing_extensions import TypedDict

DEFAULT_TIMEOUT_SECONDS = 300
CLEAN_INTERVAL_SECONDS = 5

class Order(TypedDict):
    number: int
    expiry: datetime

class OrderStore:
    def __init__(self, cleanup_interval_seconds: int = 5):
        self._orders: list[Order] = []
        self._cleanup_interval_seconds = cleanup_interval_seconds
        self._last_cleanup = datetime.now()

    def add_order(self, order_number: int, timeout_seconds: int | None = None):
        self._cleanup()

        # Calculate the datetime starting which this order should no longer be visible
        timeout = timeout_seconds if timeout_seconds is not None else DEFAULT_TIMEOUT_SECONDS
        expiry: datetime = datetime.now() + timedelta(seconds=timeout)

        self._orders.append({'number': order_number, 'expiry': expiry})

    def get_orders(self) -> list[Order]:
        self._cleanup()

        return self._orders

    def _should_cleanup(self) -> bool:
        now = datetime.now()
        diff = now - self._last_cleanup
        seconds = diff.total_seconds()
        return seconds > self._cleanup_interval_seconds

    def _cleanup(self):
        if not self._should_cleanup():
            return

        now = datetime.now()
        self._orders = [order for order in self._orders if now < order['expiry']]
