#!/bin/bash
sudo cp ./_udev_/*.rules  /etc/udev/rules.d
sudo service udev reload
sudo service udev restart
echo "done"
