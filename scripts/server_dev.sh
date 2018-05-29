#!/bin/sh

gunicorn -w 1 -b 0.0.0.0:7777 server_dev:app
