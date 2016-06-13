__author__ = 'Jitender_Jal'
import glob
import re
from mail import send_email
regx = re.compile(r"^.*&spellcheck.q=(.*)&")
# data = open("/mnt/ebs/solr-4.10.2/example/logs/solr.log","r")
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import Encoders
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import csv
regions = {
    1:"Delhi",
    2:"Gurgaon/Faridabad",
    3:"Noida/Ghaziabad",
    4:"Mumbai",
    5:"Bangalore",
    6:"Thane",
    7:"Navi Mumbai",
    8:"Mohali",
    9:"Panchkula",
    10:"Jaipur",
    12:"Chandigarh",
    13:"Ahmedabad",
    14:"Kolkata",
    15:"Hyderabad",
    16:"Chennai",
    17:"Lucknow",
    18:"Kanpur",
    19:"Ludhiana",
    20:"Indore",
    21:"Bhopal",
    22:"Nagpur",
    23:"Pune",
    24:"Pimpri-Chinchwad",
    25:"Vadodara",
    26:"Kochi",
    27:"Surat",
    28:"Howrah",
    29:"Kalyan-Dombivli",
    30:"Amritsar",
    31:"Jalandhar",
    32:"Gwalior",
    33:"Hospet",
    34:"Hubli",
    35:"Jabalpur",
    36:"Dehradun",
    37:"Gulbarga",
    38:"Coimbatore",
    39:"Erode",
    40:"Ranchi",
    41:"Salem",
    42:"Siliguri",
    43:"Aurangabad",
    44:"Bareilly",
    45:"Agra",
    46:"Allahabad",
    47:"Patna",
    48:"Pondicherry",
    49:"Ambala",
    50:"Mysore",
    51:"Asansol",
    52:"Mangalore",
    53:"Tirunelveli",
    54:"Varanasi",
    55:"Jamnagar",
    56:"Nashik",
    57:"Palakkad",
    58:"Pathanamthitta",
}

# def send_email(sub='',text=''):
#     me = 'devops@zopper.com'
#     to = ['rahul.gupta@zopper.com','mayank.gupta@zopper.com','ravi@zopper.com','roshni@zopper.com']
#
#     # Create message container - the correct MIME type is multipart/alternative.
#     msg = MIMEMultipart('mixed')
#     msg['Subject'] = sub
#     msg['From'] = me
#     msg['To'] = ','.join(to)
#
#     # body of the email
#     text=text
#     part1 = MIMEText(text, 'plain')
#     part1.add_header('Content-Disposition', 'attachment', filename="attachment.csv")
#     msg.attach(part1)
#
#     # attaching the text file
#     # if file_path:
#     #     fp = open(file_path, 'rb')
#     #     file1 = MIMEBase('application','vnd.ms-excel')
#     #     file1.set_payload(fp.read())
#     #     fp.close()
#     #     encode_base64(file1)
#     #     file1.add_header('Content-Disposition','attachment;filename=%s'%file_name)
#     #     msg.attach(file1)
#
#     # sending the email to the server
#     composed = msg.as_string()
#     username = 'devops@zopper.com'
#     password = '9rbefgD8dJfZQRl0kdMd-Q'
#     server = smtplib.SMTP('smtp.mandrillapp.com:587')
#     server.ehlo()
#     server.starttls()
#     server.login(username,password)
#     server.sendmail(me, to, msg.as_string())
#     server.quit()

if __name__ == "__main__":
    # files = glob.glob("/mnt/ebs/solr-4.10.2/example/logs/*")
    files = glob.glob("*.log")
    data = []
    for file in files:
        print file
        fdata = open(file,"r")
        lines = fdata.readlines()
        i = 0
        for line in lines:
            try:
                i = i+1
                if len(line.split("hits=0"))>1:
                    match = re.search(regx,line)
                    data.append([match.groups()[0].split("&",1)[0].replace("+"," "),regions.get(int(line.split("fq=region:")[1].split('&',1)[0]),"None")])
            except:
                pass
    print data
    result = ''
    for row in data:
        result += "\n"
        col = ""
        for data in row:
            col += data+","
        result += col
    print result
    if len(result) > 0:
        send_email(title="Zero result data" , data=result)
    # if len(data) > 0:
    #     send_email(sub="Zero result data" , text=",".join(data))
