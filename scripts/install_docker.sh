#!/usr/bin/env bash

echo 'Updating the apt'
sudo apt update

echo 'Install the certificates'
sudo apt install apt-transport-https ca-certificates curl software-properties-common

echo 'Installing Docker'
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
sudo apt install docker-ce
sudo usermod -aG docker ${USER}
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo 'Verifing the installation'
docker -v
docker-compose -v
