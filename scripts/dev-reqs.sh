# #!/bin/sh
# # For Ubuntu machines
# # --------------------------------------------
# sudo apt-get update && apt-get install -y \
#     software-properties-common
# sudo add-apt-repository multiverse
# sudo apt-get update && apt-get install -y \
#    build-essential \
#    git \
#    libpq-dev \
#    python3 \
#    python3-dev \
#    python3-pip \
#    nginx \
#    libssl-dev \
#    libjpeg-dev \
#    jpegoptim \
#    optipng \
#    gettext \
#    curl

# # For CentOS machines
# # --------------------------------------------
# # sudo yum update && sudo yum upgrade
# # sudo yum install -y \
# #     epel-release \
# #     git \
# #     libpqxx-devel \
# #     zlib \
# #     openssl-devel \
# #     python-devel \
# #     nginx \
# #     libjpeg-turbo-devel \
# #     jpegoptim \
# #     optipng \
# #     gettext \
# #     curl

# For Fedora systems

 sudo dnf install -y \
     git \
     libpqxx-devel \
     zlib \
     openssl-devel \
     python-devel \
     nginx \
     libjpeg-turbo-devel \
     jpegoptim \
     optipng \
     gettext \
     curl

 pip install --upgrade pip wheel setuptools
 pip install -r requirements/base.txt
 pip install -r requirements/production.txt
 pip install -r requirements/local.txt
 pip install -r requirements/test.txt

 sed -i 's/\r//' entrypoint-local.sh \
     && chmod +x entrypoint-local.sh \
     && chown ivan entrypoint-local.sh \
     && sed -i 's/\r//' run-local.sh \
     && chmod +x run-local.sh \
     && chown ivan run-local.sh
