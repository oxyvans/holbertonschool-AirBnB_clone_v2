#!/usr/bin/env bash
# task 0

#installs nginx
sudo apt-get update -y
sudo apt-get install nginx -y

#creates directories needed
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# fake html
echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body
</html>" > /data/web_static/releases/test/index.html

#symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership to user and group
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data

#update nginx configuration
printf %s "server {
        listen 80;
        listen [::]:80;
        add_header X-Served-By  $HOSTNAME;
        root   /var/www/html;
        index  index.html;
        location /hbnb_static {
            alias  /data/web_static/current;
            index  index.html;
        }
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        error_page 404 /5-design_a_beautiful_404_page.html;
}" > /etc/nginx/sites-available/default

sudo service nginx restart
