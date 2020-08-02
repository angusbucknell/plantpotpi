import serial, csv, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
temp_range = 20
data = []
x = 0
EmailDecider = False

ser = serial.Serial("/dev/ttyACM0")

def SendEmail(rx, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("plantpi.info@gmail.com", "plantcool")
    contents = content.as_string()
    server.sendmail("plantpi.info@gmail.com", rx, contents)
    server.quit()

def CompileEmail(rx,subj,info):
    message = MIMEMultipart()
    message["From"] = "plantpi.info@gmail.com"
    message["To"] = rx
    message["Subject"] = subj
    message.attach(MIMEText(info, "plain"))
    SendEmail(rx,message)

while True:
    if x > 2:
        data_file = open("/var/www/html/testdata.txt","a")
        data_recorder = csv.writer(data_file)
        data_recorder.writerow([data[0],data[1],data[2],50])
        data_file.close()
        print("Making decision now")
        if int(data[0]) > temp_range:
            EmailDecider = True
            print("Will send an email!")
        x = 0
        data = []
    if EmailDecider == True:
        print("Starting process")
        CompileEmail("angus.bucknell@qehpupil.co.uk","Plant Temperature Warning",
                   "Your plant temperature is over "+ str(temp_range)+" degrees!")
        print("Done!")
        EmailDecider = False
        #Watering plant part
    if data[3] == True:
        print("Plant has been watered!") 
        
    if ser.in_waiting > 0:
        data.append(ser.readline().strip().decode())
        x = x + 1
        print(x)
        print(data)
