#!/bin/sh

sudo apt-get update
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y


git clone https://www.github.com/CiscoSE/devnet-2126.git
cd devnet-2126/nso_clive-portal/
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate

#To run the web server use the following command in the nso_clive-portal directory
#python3 manage.py runserver 0.0.0.0:8080
#on your local machine go to http://localhost:2200 to use the portal
