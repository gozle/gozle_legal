#!/bin/bash

# Run migrations
python manage.py migrate

python manage.py createsuperuser

# Start Django development server
exec "$@"
