import serial, csv, smtplib
#Used pySerial library to recieve transmitted data
#Used csv library to write to file in correct formatted
#smtp library used to send email via SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Used for constructing multipart email messages
from datetime import datetime
#Used to write date stamp on data record
temp_range = 20
#Limiter to base whether email needs to be send out
data = []
#Initialises empty array which data will be transferred to
x = 0
#Initalises variable to see what data has been transmitted so far per record
EmailDecider = False
#Flag initalised to see if email should be sent

ser = serial.Serial("/dev/ttyACM0")
#Selects which port to listen to

def SendEmail(rx, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
#Established connection with Gmail SMTP server
    server.starttls()
#Secures connectionusing TLS
    server.login("plantpi.info@gmail.com", "plantcool")
#Logins into TX Gmail account
    contents = content.as_string()
#Adds function argument as email message
    server.sendmail("plantpi.info@gmail.com", rx, contents)
#Sends email from Gmail account to specified email address
    server.quit()
#Terminates connection to Gmail

def CompileEmail(rx,subj,info):
#Compiles multipart message, this happens before SendEmail
    message = MIMEMultipart()
#Creates new multipart message
    message["From"] = "plantpi.info@gmail.com"
#Attaches transmitting email address
    message["To"] = rx
#Attaches recieving email address from function arg
    message["Subject"] = subj
#Attaches subject from function argument
    message.attach(MIMEText(info, "plain"))
#Attaches text to the message
    SendEmail(rx,message)
#Calls function to send the email

while True:
    if x > 2:
        data_file = open("/var/www/html/testdata.txt","a")
#Opens text file to input data into for website, "a" appends to bottom of file
        data_recorder = csv.writer(data_file)
#Sets up to write data in CSV format to file
        current_day = datetime.today().strftime("%Y-%m-%d")
#Assigns var to current date in YYYY-MM-DD format
        print(current_day)
#Prints date for testing purposes
        data_recorder.writerow([data[0],data[1],data[2],50,current_day])
#Appends new row of data to file
        data_file.close()
#Closes access to file
        print("Making decision now")
#Needed for testing
        if int(data[0]) > temp_range:
#Checks to see if current temperature is above the limit
            EmailDecider = True
            print("Will send an email!")
#Needed for testing
        x = 0
        data = []
#Resets variables for next set of data to be recieved
    if EmailDecider == True:
        print("Starting process")
        CompileEmail("angus.bucknell@qehpupil.co.uk","Plant Temperature Warning",
                   "Your plant temperature is over "+ str(temp_range)+" degrees!")
#Sends email with necessary arguments
        print("Done!")
        EmailDecider = False
#Resets flag for next set of data
    if ser.in_waiting > 0:
#Checks to see if data is waiting in Serial buffer
        data.append(ser.readline().strip().decode())
##Cleans data and appends to array
        x = x + 1
        print(x)
        print(data)
