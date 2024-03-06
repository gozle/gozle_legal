#!/bin/bash

# Run migrations
python3 manage.py makemigrations accounts documents
python3 manage.py migrate


# Start Django development server
exec "$@"
