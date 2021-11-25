#!/bin/bash

set -e

./water-overflow/manage.py migrate
./water-overflow/manage.py collectstatic --noinput

exec tail -f /dev/null
