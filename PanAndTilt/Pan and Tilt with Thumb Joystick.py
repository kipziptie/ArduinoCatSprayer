#
#
#
#Resources
# line.strip; BYTE type; https://docs.python.org/3/library/stdtypes.html
# Servo PWM explained: https://www.teachmemicro.com/raspberry-pi-pwm-servo-tutorial/
# Servo DataSheet: http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf
# 
from time import sleep # for sleep function
import RPi.GPIO as GPIO
import subprocess
import smbus

channel = 1
addresspan = 0x05
addresstilt = 0x04
reg_write_dac = 0x40
bus = smbus.SMBus(channel)

### Video Stream via VLC ###
#
# pid = subprocess.run("vlc v4l2:///dev/video0 --v4l2-standard --live-caching 20 --zoom .5 &", shell=True)
#
############################

XPIN = 17
YPIN = 18
xStartPosition = 27
yStartPosition = 26
frequency = 200
#pwmSetMode(PWM_MODE_MS)
GPIO.setmode(GPIO.BCM)
GPIO.setup(XPIN, GPIO.OUT)
GPIO.setup(YPIN, GPIO.OUT)
p = GPIO.PWM(XPIN, frequency) # PWM with 50Hz on servoPIN
p.start(xStartPosition)

q = GPIO.PWM(YPIN, frequency) # PWM with 50Hz on servoPIN

q.start(yStartPosition)

## Retire this function
def PAN_position(desired):
    position = convert_thumbstick_to_servo(int(desired))
    #p.start(1)
    #p.ChangeDutyCycle(int(slider_value))
    print("Pan: ", position)
    q.ChangeDutyCycle(position)
    #bus.write_byte(address, position)
    print(position)
    
## Retire this function
def TILT_position(desired):
    position = convert_thumbstick_to_servo(int(desired))
    #p.start(1)
    #p.ChangeDutyCycle(int(slider_value))
    print("Tilt: ", position)
    p.ChangeDutyCycle(position)

def set_PAN_TILT_Position(XYtuple):
    bus.write_byte(address, XYtuple)

def convert_thumbstick_to_servo(pValue):
    
    OldMax = 1025
    OldMin = 0
    NewMax = 180
    NewMin = 1
    
    OldRange = (OldMax - OldMin)  
    NewRange = (NewMax - NewMin)  
    NewValue = (((pValue - OldMin) * NewRange) / OldRange) + NewMin
    
    #position = ( int(pValue) % 13 )  
    position = int(NewValue)
    #print("Position",position)
    return position
  

# Writes a random byte to the arduino to establih connectivity
def wakeTheArduino():
    ser.write(b"l")
    
    

import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
wakeTheArduino() # call once to stop receiving (0,0) messages from the Arduino
ser.flushInput()

# Returns a string. Be sure to call wakeTheArduino() First
#Fetches controller status from Arduino as Bytes
#THEN encodes those bytes to an ASCII string
#Then removes the Carriage Return newline
def getControllerInput():
    wakeTheArduino()
    # adds a string to the serial read buffer, which was sent by the Arduino
    input = ser.readline()
    return byteToString(input.strip())

# Prints the junk sent by the Arduino Joystick controller
def printControllerInput(XY):
    #print (XY)
    myTuple = XY.split(",")
    X = myTuple[0]
    Y = myTuple[1]

    print ("X: ", X, "\nY: ", Y)
    print ("(X,Y)", X,Y)


# Returns a Tuple of X and Y
# use X = myTuple[0]
# and Y = myTuple[1]
# to break them out in other functions
def getControllerStatusTuple():
    XY = getControllerInput()
    #printControllerInput(XY)
    myTuple = list(map(int,XY.split(",")))
    return myTuple

def printTuple(inp):
    for i in inp:
        print (i)

def printXY(inp):
    print ("(X,Y)", inp[0], inp[1])
    
def stringToByte(inp):
    out = bytes(inp, "utf-8")
    return out

def byteToString(inp):
    out = inp.decode("utf-8")
    return out

def updatePosition(XY):
    #sendstring=''.join(XY)
    print("TYPE: ", type(XY[0]))
    positiontilt = convert_thumbstick_to_servo(XY[0])
    positionpan = convert_thumbstick_to_servo(XY[1])
    #print("list(TYPE): ", type(list(XY[0])))
    
    #bus.write_i2c_block_data(address, 0xf0, XY)
    bus.write_byte(addresstilt, positiontilt)
    bus.write_byte(addresspan, positionpan)
    #for i in XY:
    #    bus.write_byte(address, int(i, base=16))
        
    #    sleep(.1)
    #    print(i)
#import matplotlib.pyplot
#matplotlib.pyplot.show()
#matplotlib.pyplot.ion()
#xplot = [0]
#yplot = [0]
myTuple = (xStartPosition, yStartPosition)    
while True:
    sleep(.1)
    oldTuple = myTuple
    myTuple = getControllerStatusTuple()
    
    if (abs(int(myTuple[0]) - int(oldTuple[0])) > 2):
        print("OLD:", oldTuple[0], "NEW:", myTuple[0])
        ## Retire this function - PAN_position(myTuple[0])
        updatePosition(myTuple)
        
    if (abs(int(myTuple[1]) - int(oldTuple[1])) > 2 ):
        print("SENT:", "OLD:", oldTuple[1], "`nNEW:", myTuple[1])
        ## Retire this function - TILT_position(myTuple[1])
        updatePosition(myTuple)
        
        
    #printControllerInput(getControllerInput())
    #printXY(getControllerStatusTuple())
    
    #printTuple(myTuple)
    #xplot.append(myTuple[0])
    #yplot.append(myTuple[1])
    #matplotlib.pyplot.plot(xplot,yplot, marker='o')
    
    
    
    
    #matplotlib.pyplot.draw()
    #matplotlib.pyplot.pause(0.001)
    
    #matplotlib.pyplot.show()
    
    
    