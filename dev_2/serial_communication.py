#Outputs Arduino data in formatted "nice" fashion to a text file
#Arduino sends data one after the other: Temp1, Hum1, Soil1, Temp2, Hum2...
#Text file requires each set (Temp1, Hum1, Soil1) to be on one line separated by tabs

import serial 
#Uses pySerial library
data = [] 
#Initialises array which data is organised into
x = 0 
#Initialises counter
ser = serial.Serial("/dev/ttyACM0") 
#Assigns variable to USB port
while True:
    if x > 2: 
#Differentiates between each set of data
        file = open("test.txt", "w") 
#Opens text file to input data into
        file.write(data[0]+"\t") 
#Writes temperature to top line of file
        file.write(data[1]+"\t") 
#Writes humidity after a tab on the same line
        file.write(data[2]+"\n") 
#Writes soil moisture after a tab and then returns to new line
        file.close() 
        x = 0 
        data = [] 
#Resets array with data which has been written
    if ser.in_waiting > 0: 
#Checks to see if data is waiting in Serial buffer
        data.append(ser.readline().strip().decode()) 
#Cleans data and appends to array
        x = x + 1 
#Increments counter
        print(x) 
#Prints counter to screen, only for testing
        print(data) 
#Prints data to screen, only for testing


        
