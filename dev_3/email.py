import smtplib
#Uses SMTP library to send emails
from email.mime.multipart import MIMEMultipart
#Imports function to create multipart emails
from email.mime.text import MIMEText
#Imports function to create multipart emails

def SendBasicEmail(FromEmail, ToEmail, Contents, Pword):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(FromEmail, Pword)
    server.sendmail(FromEmail, ToEmail, Contents)
    server.quit()
#SendBasicEmail is the previously developed model

def SendProperEmail(FromEmail,ToEmail,Subject,Contents,Pword):
#Sends multipart email using provided arguments
    sendit = MIMEMultipart()
#Calls function to create subclass for multipart
    sendit['From'] = FromEmail
#Defines sender to argument passed in function
    sendit['To'] = ToEmail
#Defines reciever as argument passed in function
    sendit['Subject'] = Subject
#Defines the email subject from the function argument
    sendit.attach(MIMEText(Contents, 'plain'))
#Attaches message payload from function argument to the email
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(FromEmail, Pword)
#Accesses email client same as previous method
    text = sendit.as_string()
#Redeclared multipart email as text to be sent
    server.sendmail(FromEmail, ToEmail, text)
#Sends the multipart message using given arguments
    server.quit()
#Closes connection to email client

SendProperEmail("XXX", "XXX", "Raspberry Pi!", "Test", "XXX")
    
