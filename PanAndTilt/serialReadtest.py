#
#
#
#Resources
# line.strip; BYTE type; https://docs.python.org/3/library/stdtypes.html
# 
from time import sleep # for sleep function

# Writes a random byte to the arduino to establih connectivity
def wakeTheArduino():
    ser.write(b"l") 

import serial
ser = serial.Serial('/dev/ttyACM2', 9600)
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
    myTuple = XY.split(",")
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



while True:
    sleep(.25)
    #printControllerInput(getControllerInput())
    printXY(getControllerStatusTuple())
    