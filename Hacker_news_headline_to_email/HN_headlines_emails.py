import requests  # http requests

from bs4 import BeautifulSoup  # web scraping

# send email
import smtplib

# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SYSTEM Date and time manipulation
import datetime

now = datetime.datetime.now()

# email content placeholder

content = ''

# Extracting Hacker News Stories


def extract_news(url):
    print('Extracting Hacker News Stories.....')
    cnt = ''  # Placeholder Used to hold the email too
    cnt += ('<b>HN Top StoriesL<b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        if tag.text != 'More':
            cnt += (str(i+1) + ' :: ' + tag.text + "\n" + '<br> ')
        else:
            cnt += ''

    return(cnt)


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

# Sending the Emails
print('Composing Email')

#update your email details
SERVER = 'smtp.gmail.com' #"your smtp server"
PORT = 587 #your port number
FROM = 'jackyyeh1999@gmail.com' #your sender email address
TO = 'jackyyeh1999@gmail.com' #your receiver email address
PASS = '5456575753575651' #Your receiver password


#Message Body
#The message body object initiated to send contents
msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content,'html'))

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(0) #To enable whether to see the debuging or error messages when sending mails
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())

print('Email Sent')

server.quit()
