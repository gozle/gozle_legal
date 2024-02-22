#!/bin/bash

# Run migrations
python manage.py migrate

# Start Django development server
exec "$@"
