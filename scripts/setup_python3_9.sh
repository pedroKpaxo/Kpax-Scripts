#!/usr/bin/env bash

echo 'Starting command'
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9

echo 'Getting distutils'
sudo apt install python3.9-distutils

echo 'Getting pip'
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py