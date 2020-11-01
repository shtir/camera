#! /usr/bin/env python
import picamera
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (2560,1936)
camera.rotation = 90
camera.start_preview()
sleep(5)
camera.capture('/var/www/html/pic/test.jpg')
camera.stop_preview()
