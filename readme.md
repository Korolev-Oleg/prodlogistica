# E-comerce website for company "Prodlogistica South"
>djangocms / python
## Deployment django to web server
##### First we need create user:
````
adduser www
usermod -aG sudo www
````
##### Configure SSH:
````
sudo vim /etc/ssh/sshd_config
    AllowUsers www
    PermitRootLogin no
    PasswordAuthentication no

sudo service ssh restart
````
##### Init — packages & ZSH:
````
sudo apt-get install -y zsh tree redis-server nginx  libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-dev python-imaging python3-lxml libxslt-dev python-libxml2 python-libxslt1 libffi-dev libssl-dev python-dev gnumeric libsqlite3-dev libpq-dev libxml2-dev libxslt1-dev libjpeg-dev libfreetype6-dev libcurl4-openssl-dev supervisor
````
###### nstall oh-my-zsh:
