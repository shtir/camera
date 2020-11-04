#! /usr/bin/env python
import picamera
from time import sleep
from picamera import PiCamera
import os.path
from datetime import datetime
import os

# stop RTSP
f = os.popen('sudo systemctl stop rtsp-stream.service')

# varible 
directory = "/var/www/html/camera/"


# check main directory folder existeing
if not os.path.exists(directory):
    os.makedirs(directory)

# generate date an time folder
today = datetime.now()
todayeFolder = today.strftime("%Y-%m-%d")
if not os.path.exists(directory+todayeFolder):
    os.makedirs(directory+todayeFolder)

picaddress = directory+todayeFolder+"/"+today.strftime('%H%M%S')+".jpg"

#print(picaddress)

camera = PiCamera()
camera.resolution = (2560,1936)
camera.rotation = 90
camera.start_preview()
sleep(5)
camera.capture(picaddress)
camera.stop_preview()




# start RTSP
f = os.popen('sudo systemctl start rtsp-stream.service')
