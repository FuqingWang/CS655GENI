#!/bin/bash

# Install pip3
sudo add-apt-repository universe
sudo apt-get update
sudo apt-get install -y python3-pip

# Install wget
sudo pip3 install wget

mkdir result

# Measure time elapsed without cache and with cache, attention the order
python3 timeWithoutCache.py
python3 timeWithCache.py