#!/bin/sh
source venv/bin/activate
python manage.py db upgrade
exec python app.py