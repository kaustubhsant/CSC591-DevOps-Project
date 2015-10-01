#!/bin/bash


# Install Jenkins dependency and start Jenkins
sudo wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update -y 
sudo apt-get install jenkins git -y
git config --global http.sslverify false 
sudo service jenkins start

sudo sh -c "echo \"jenkins ALL=(ALL) NOPASSWD:ALL\" >> /etc/sudoers"

#Install python and pip package manager
sudo apt-get install python -y
sudo apt-get install python-pip -y

#Install proxy which can redirect calls to Jenkin Service End points
sudo apt-get install apache2 -y 
sudo a2enmod proxy
sudo a2enmod proxy_http

sudo sh -c "echo \"<VirtualHost *:80>
    ServerName ec2-52-89-232-35.us-west-2.compute.amazonaws.com
    ProxyRequests Off
    <Proxy *>
        Order deny,allow
        Allow from all
    </Proxy>
    ProxyPreserveHost on
    ProxyPass / http://localhost:8080/
</VirtualHost>\" > /etc/apache2/sites-available/jenkins.conf"

sudo a2ensite jenkins
sudo service apache2 reload
