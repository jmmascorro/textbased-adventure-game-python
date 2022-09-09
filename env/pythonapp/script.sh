#!/bin/bash

echo -------------- Update source list --------------
sudo apt-get update -y

echo -------------- Install Python ------------------
sudo apt-get install software-properties-common -y

echo ------------- Installing Apache ----------------
sudo apt install apache2 -y

echo ------------ Enabling Apache Proxy -------------
sudo a2enmod proxy
sudo a2enmod proxy_http

echo ------- Add nology Apache Proxy File -----------
cp /home/vagrant/env/nodeapp/nology-proxy.conf /etc/apache2/sites-available
echo ls -la /etc/apache2/sites-available

echo ------- Register nology Apache Proxy File ------
sudo a2ensite nology-proxy.conf

echo -------------- Restart Apache ------------------
sudo systemctl reload apache2

echo --------------- Move into App Folder -----------
cd ../vagrant/app
pwd

echo -------------- Install Dependencies ------------
sudo apt-get install python3-pandas -y

# echo ------------- Run App -------------------
# python3 text_adventure.py
