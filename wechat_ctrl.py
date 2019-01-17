#!/usr/bin/env python
#coding=utf8
import os
import itchat
@itchat.msg_register(itchat.content.TEXT)
def callback(msg):
    if msg['Text'] == u'启动底盘':
	os.system('echo "ros" |sudo -S systemctl start chassis.service')
    if msg['Text'] == u'关闭底盘':
	os.system('echo "ros" |sudo -S systemctl stop chassis.service')

    if msg['Text'] == u'启动雷达':
	os.system('echo "ros" |sudo -S systemctl start lidar.service')
    if msg['Text'] == u'关闭雷达':
	os.system('echo "ros" |sudo -S systemctl stop lidar.service')

    if msg['Text'] == u'启动语音':
	os.system('echo "ros" |sudo -S systemctl start voice.service')
    if msg['Text'] == u'关闭语音':
	os.system('echo "ros" |sudo -S systemctl stop voice.service')

    if msg['Text'] == u'启动遥控':
	os.system('echo "ros" |sudo -S systemctl start teleopjoy.service')
    if msg['Text'] == u'关闭遥控':
	os.system('echo "ros" |sudo -S systemctl stop teleopjoy.service')

    if msg['Text'] == u'启动键盘':
	os.system('echo "ros" |sudo -S systemctl start keyboard.service')
    if msg['Text'] == u'关闭键盘':
	os.system('echo "ros" |sudo -S systemctl stop keyboard.service')

    if msg['Text'] == u'启动摄像头':
	os.system('echo "ros" |sudo -S systemctl start camera.service')
    if msg['Text'] == u'关闭摄像头':
	os.system('echo "ros" |sudo -S systemctl stop camera.service')

    if msg['Text'] == u'启动点云跟随':
	os.system('echo "ros" |sudo -S systemctl start pcl_follow.service')
	os.system('echo "ros" |sudo -S systemctl start camera.service')
	os.system('echo "ros" |sudo -S systemctl start camera.service')
    if msg['Text'] == u'关闭点云跟随':
	os.system('echo "ros" |sudo -S systemctl stop pcl_follow.service')

    if msg['Text'] == u'关闭所有':
	os.system('echo "ros" |sudo -S systemctl stop chassis.service')
	os.system('echo "ros" |sudo -S systemctl stop teleopjoy.service')
	os.system('echo "ros" |sudo -S systemctl stop lidar.service')
	os.system('echo "ros" |sudo -S systemctl stop voice.service')
	os.system('echo "ros" |sudo -S systemctl stop keyboard.service')
	os.system('echo "ros" |sudo -S systemctl stop camera.service')
	os.system('echo "ros" |sudo -S systemctl stop pcl_follow.service')

    if msg['Text'] == u'上传固件':
	os.system('/mxBot_ws/src/mx_turtleBot/mx_chassis/ros_arduino_firmware/upload_arduino_hex/upload.sh')
	     
if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()


