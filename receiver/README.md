# Hubble Order Tracker - Receiver

This folder contains the receiver for the Hubble Food Tracker. The receiver
contains an endpoint for the StarCommunity order webhook, which is used to
receive orders. Clients can then request the list of active orders from the
receiver. Orders have a lifespan of 5 minutes, after which they are deleted
from the in-memory store.

## Installation
- Create a new virtual environment (Python 3.11+).
- `pip install -r requirements.txt`
- In the `./src` folder, run `fastapi dev api.py`.

You can find the API specification on [http://localhost:8000/docs](http://localhost:8000/docs).
