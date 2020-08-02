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
#Differentiates between each set of data, will be 3 when Lux included
        file = open("/var/www/html/testdata.txt", "a")
#Opens text file to input data into for website, "a" appends to bottom of file
        file.write(data[0]+"\t") 
#Writes temperature to top line of file
        file.write(data[1]+"\t") 
#Writes humidity after a tab on the same line
        file.write(data[2]+"\t") 
#Writes soil moisture after a tab
        file.write("70"+"\n") 
#Placeholder for Lux data
        file.close() 
#Closes file to save it after writing
        x = 0 
#Resets counter to start at new set
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
