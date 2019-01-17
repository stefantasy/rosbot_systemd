#!/bin/bash
sudo cp -r aikit_shell/ /usr/local/bin/
sudo cp service/*.service /lib/systemd/system/
sudo systemctl daemon-reload
cp wechat_ctrl.py  /home/intel/mxBot_ws/src/mx_turtleBot/mx_test/script/



