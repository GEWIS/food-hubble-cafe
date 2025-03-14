# Hubble Food Tracker

This repository contains the source code for the new Hubble Food Tracker.
The system receives finished orders from StarCommunity using a webhook,
which are then propagated to all listening clients.

## Structure
The Hubble Food Tracker consists of two parts.
- The [frontend](./frontend) contains the interface that people use to see
the most recent finished orders.
- The [receiver](./receiver) contains the backend that receives finished
orders. The frontend can then request a list of all active orders.

## Deployment
Running the Hubble Food Tracker in production is done using Docker Compose.
If you have cloned the repository locally, you can build and start the
project by running `docker-compose up`. You can also run the Hubble Food
Tracker anywhere else by simply using the published images. Note that you
do have to update the docker-compose file to point to the correct image locations.

## License
Hubble Food Tracker uses the [AGPL-v3 license](./LICENSE).

## Copyright
© 2025 - Study Association GEWIS & Hubble Community Café
