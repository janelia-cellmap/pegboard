#!/bin/sh

echo "Waiting for pegdb..."

while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done

echo "pegdb started"

python manage.py flush --no-input
python manage.py migrate

exec "$@"
