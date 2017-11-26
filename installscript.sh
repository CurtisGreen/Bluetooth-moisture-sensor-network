#!/bin/bash
sudo apt-get --yes --force-yes install libglib2.0-dev
sudo apt-get --yes --force-yes install libbluetooth-dev
sudo apt-get --yes --force-yes install libboost-python-dev
sudo apt-get --yes --force-yes install libboost-thread-dev
sudo apt-get --yes --force-yes install libboost-dev
sudo apt-get --yes --force-yes purge python-bson
sudo apt-get --yes --force-yes install python-bson
sudo python setup.py install
sudo pip install gattlib
sudo pip uninstall bson
sudo pip uninstall pymongo
sudo pip install pymongo
sudo pip install gattlib
sudo pip install -—upgrade setuptools
sudo reboot