import datetime
import time
import os
#import serial
import pickle
import numpy as np
from scipy.io import loadmat
import RPi.GPIO as GPIO
#import picamera

#camera=picamera.PiCamera()
fwd=18
bwd=23
right=25
left=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(fwd,GPIO.OUT)
GPIO.setup(bwd,GPIO.OUT)
GPIO.setup(right,GPIO.OUT)
GPIO.setup(left,GPIO.OUT)

#ser=serial.Serial('/dev/ttyACM0',9600)

f=open('/home/pi/car1.txt','rb')
clf=pickle.load(f)

def MoveLeft():
    print('left predicted')
    GPIO.output(left,True)
    GPIO.output(fwd,True)
    time.sleep(0.35)
    Stop()
    #val='768'
    #ser.write(bytes(val.encode('ascii')))
    
def MoveRight():
    print('right predicted')
    GPIO.output(right,True)
    GPIO.output(fwd,True)
    time.sleep(0.25)
    Stop()
    #val='256'
    #ser.write(bytes(val.encode('ascii')))

def MoveForward():
    print('forward predicted')
    GPIO.output(fwd,True)
    time.sleep(0.25)
    Stop()
    #val='512'
    #ser.write(bytes(val.encode('ascii')))

def MoveBackward():
    print('backward predicted')
    GPIO.output(bwd,True)
    time.sleep(0.25)
    Stop()
    #val='512'
    #ser.write(bytes(val.encode('ascii')))

def Stop():
    print('stop')
    GPIO.output(left,False)
    GPIO.output(right,False)
    GPIO.output(fwd,False)
    GPIO.output(bwd,False) 
    #val='0'
    #ser.write(bytes(val.encode('ascii')))


def forward_propagate():
    #os.system('octave p.m')
    test=loadmat("p.mat")
    Xtest = test['m']
    Xtest = [(x/255.0) for x in Xtest]
    Xtest = np.matrix(Xtest)
    pred=clf.predict(Xtest)
    return pred[0]        



r=('/home/pi/pred/img.jpg')
#camera.capture(r)
#os.system('sudo mogrify -resize 20x20 /home/pi/pred/img.jpg')
i=0
i=forward_propagate()
print(i)
if(i==1):
    MoveBackward()
if(i==2):
    MoveForward()
if(i==3):
    MoveLeft()
if(i==4):
    MoveRight()
time.sleep(2)        
        



    

