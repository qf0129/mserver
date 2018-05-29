#!/bin/bash

gunicorn -w 1 -b 127.0.0.1:7777 main:app
