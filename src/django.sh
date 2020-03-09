#!/usr/bin/env bash

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "$POSTGRES_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

python manage.py collectstatic --noinput --clear > /dev/null 2>&1
python manage.py migrate

if [ "$DEBUG" == "true" ]; then
#  gunicorn --workers=4 --bind=0.0.0.0:8000 --reload menu_example.wsgi:application
  python manage.py runserver 0.0.0.0:8000
else
  gunicorn --workers=4 --bind=0.0.0.0:8000 menu_example.wsgi:application
fi
