FROM nginx:latest

RUN mkdir /usr/share/nginx/html/.well-known
RUN echo  "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y software-properties-common curl vim
