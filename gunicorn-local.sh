#!/bin/sh
sudo apt-get update && apt-get install -y \
    software-properties-common
sudo add-apt-repository multiverse
sudo apt-get update && apt-get install -y \
   build-essential \
   git \
   libpq-dev \
   python3 \
   python3-dev \
   python3-pip \
   nginx \
   libjpeg-dev \
   jpegoptim \
   optipng \
   gettext \
   curl

pip install -r requirements/base.txt
pip install -r requirements/production.txt
pip install -r requirements/local.txt
pip install -r requirements/test.txt

sed -i 's/\r//' entrypoint-local.sh \
    && sed -i 's/\r//' gunicorn-local.sh \
    && chmod +x entrypoint-local.sh \
    && chown ivan entrypoint-local.sh \
    && chmod +x gunicorn-local.sh \
    && chown ivan gunicorn-local.sh

npm install \
&& npm run build \
&& python3 manage.py collectstatic --noinput \
&& python3 manage.py compilemessages \
&& python3 manage.py migrate \
&& python3 manage.py runserver
#&& sudo /usr/local/bin/gunicorn wsgi -w 4 -b 127.0.0.1:8000 --chdir=/config
