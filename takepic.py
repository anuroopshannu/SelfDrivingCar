import picamera
import os
camera=picamera.PiCamera()
   
r=('/home/pi/pred/img.jpg')
camera.capture(r)
os.system('mogrify -resize 20x20! /home/pi/pred/img.jpg')

