#!/bin/sh
npm install &&
npm run build &&
python3 manage.py collectstatic --noinput &&
python3 manage.py compilemessages &&
python3 manage.py migrate &&
/usr/local/bin/gunicorn config.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/
