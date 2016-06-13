__author__ = 'Jitender_Jal'

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import Encoders
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from datetime import date , timedelta
from smtplib import SMTPException

def send_email(title="",data=""):
    me = 'akash.mangla@zopper.com'
    to = ['jitender.jal@zopper.com']#,'archana@zopper.com','rahul.gupta@zopper.com','siddharth@zopper.com']

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('mixed')
    msg['Subject'] = title
    msg['From'] = me
    msg['To'] = ','.join(to)

    # body of the email
    text="nothin"
    part1 = MIMEText(text, 'plain')
    msg.attach(part1)

    # attaching the text file
    if data:
        file1 = MIMEBase('application','vnd.ms-excel')
        file1.set_payload(data)
        encode_base64(file1)
        file1.add_header('Content-Disposition','attachment;filename=%s'%"attachment.csv")
        msg.attach(file1)

    # sending the email to the server
    composed = msg.as_string()
    username = 'devops@zopper.com'
    #password = 'KfWVyYOVtCoK3DPj53EvSA'
    password='9rbefgD8dJfZQRl0kdMd-Q'
    server = smtplib.SMTP('smtp.mandrillapp.com:587')
    server.ehlo()
    #server.starttls()
    server.login(username,password)
    server.sendmail(me, to, msg.as_string())
    server.quit()

if __name__=='__main__':
    #tomorrowdate = `date --date="-1 days ago" "+%F"`
    send_email(title="zero result",data="nothing is there")