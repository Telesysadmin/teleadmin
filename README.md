letsencrypt:
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install certbot

$ sudo certbot certonly --webroot -w /var/www/example -d example.com