import smtplib
#Uses the SMTP library functions to send email
def SendEmail(FromEmail, ToEmail, Contents, Pword):
#Defines function to send email, with needed arguments
    server = smtplib.SMTP('smtp.gmail.com', 587)
#Begins SMTP connection to Google Mail via port 587
    server.starttls()
#Encrypts connection using Transport Layer Security
    server.login(FromEmail, Pword)
#Attempts to login into Google Mail with provided arguments
    server.sendmail(FromEmail, ToEmail, Contents)
#Sends email with message from provided arguments
    server.quit()
#Closes the SMTP connection

SendEmail("XXX", "XXX","Hey there\nTesting 123....","XXX")
#Calls the function for testing, sensitive data is removed.
