#!/usr/bin/env bash
# Install and configure a nginx server

# Install nginx
sudo apt-get update -y
sudo apt-get install nginx -y

# Create folderss
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create html index page
sudo touch /data/web_static/releases/test/index.html
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Grant user permission
sudo chown -R ubuntu:ubuntu /data/

# Configure to serve static site over /hbnb_static/
sudo sed -i '38i\ \tlocation /hbnb_static/ {\n \t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

# Restart server
sudo service nginx restart
