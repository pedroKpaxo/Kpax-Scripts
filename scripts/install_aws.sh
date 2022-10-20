#!/usr/bin/env bash

echo 'Downloading AWS_CLI'
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

echo 'Unziping the contents'
unzip awscliv2.zip

echo 'Installing AWS CLI'
sudo ./aws/install

echo 'Verifing the installation'
aws --version
