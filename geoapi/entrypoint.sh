#!/bin/sh

# Installing spatial dependencies



cd geoapi
python3 manage.py flush --no-input
python3 manage.py makemigrations --noinput
python3 manage.py migrate
python3 manage.py loaddata objects.json

exec "$@"
