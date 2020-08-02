import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendBasicEmail(FromEmail, ToEmail, Contents, Pword):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(FromEmail, Pword)
    server.sendmail(FromEmail, ToEmail, Contents)
    server.quit()
#SendEmail("ahbucknell@gmail.com", "angus.bucknell@qehpupil.co.uk","Hey there\nTesting 123....","oxysystrsh")

def SendProperEmail(FromEmail,ToEmail,Subject,Contents,Pword):
    sendit = MIMEMultipart()
    sendit['From'] = FromEmail
    sendit['To'] = ToEmail
    sendit['Subject'] = Subject
    sendit.attach(MIMEText(Contents, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(FromEmail, Pword)
    text = sendit.as_string()
    server.sendmail(FromEmail, ToEmail, text)
    server.quit()

#SendProperEmail("ahbucknell@gmail.com", "angus.bucknell@qehpupil.co.uk", "Raspberry Pi!", "Oh hey there my dudes", "oxysystrsh")

def SendEmail(tx, rx, pwd, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(tx, pwd)
    contents = content.as_string()
    server.sendmail(tx, rx, contents)
    server.quit()


def CompileEmail(tx,rx,subj,info,pwd):
    message = MIMEMultipart()
    message["From"] = tx
    message["To"] = rx
    message["Subject"] = subj
    message.attach(MIMEText(info, "plain"))
    SendEmail(tx,rx,pwd,message)



CompileEmail("ahbucknell@gmail.com","angus.bucknell@qehpupil.co.uk","Round 2","Hello World", "oxysystrsh")
