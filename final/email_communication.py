import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendEmail(rx, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("XXX", "XXX")
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
