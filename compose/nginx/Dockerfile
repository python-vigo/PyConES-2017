#
#
# Configuración manual Let's encrypt Pyday

#
# 1- Entrar en la máquina nginx

# docker exec -it pydaygal-nginx bash

# 2 - Añadir directorio well-known

# mkdir /usr/share/nginx/html/.well-known

# 3 - Actualizar sources y paquetes
# echo  "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
# apt-get update
#  apt-get install -y software-properties-common curl vim
# apt-get install certbot -t jessie-backports

# 4 - Añadir well-known a nginx
# Nginx config
# vim /etc/nginx/nginx.conf
# location /.well-known {
#     alias /usr/share/nginx/html/.well-known;
# }

# 5 - Solicitar certificados

#  certbot certonly --webroot --webroot-path /usr/share/nginx/html -d pyday2017.python-vigo.es

# 6 - Configurar  nginx
ADD ./compose/nginx/nginx.conf /etc/nginx/nginx.conf

FROM nginx:latest

RUN mkdir /usr/share/nginx/html/.well-known
RUN echo  "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y software-properties-common curl vim
RUN apt-get install certbot -t jessie-backports

RUN certbot certonly --webroot --webroot-path /usr/share/nginx/html -d pyday2017.python-vigo.es

# Nginx config
ADD ./compose/nginx/nginx.conf /etc/nginx/nginx.conf

RUN service nginx reload
