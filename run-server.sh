#!/bin/sh
daphne -b 0.0.0.0 axon_server.asgi:application
