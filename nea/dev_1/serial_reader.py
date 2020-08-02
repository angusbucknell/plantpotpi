#Read Serial input from Arduino

import serial
#Imports Serial library to read from USB

ser = serial.Serial("/dev/ttyACM0")
#Specifies which USB port to listen to
while True:
#Loops until program is terminated
    if ser.in_waiting > 0: 
#Checks to see if there is any unread input from Serial buffer
        print(ser.readline().strip().decode()) 
#If so, reads Serial buffer input and outputs to terminal
