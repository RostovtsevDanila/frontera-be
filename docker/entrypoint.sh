#!/bin/sh

python manage.py migrate || exit 1
python manage.py runserver 0.0.0.0:8000 --settings=application.settings_local
