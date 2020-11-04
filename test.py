#! /usr/bin/env python
import os
f = os.popen('sudo systemctl start rtsp-stream.service')
now = f.read()
print (now)
