# Import smtplib for the actual sending function
import smtplib
import sys
import json
import redis
import os

# Import the email modules we'll need
from email.mime.text import MIMEText

with open("config/config.json",'r') as cfg:
	config = json.load(cfg)

host = os.getenv('DB_PORT_6379_TCP_ADDR')
rserver = redis.StrictRedis(host=host,port=6379)
rserver.lrem('server',1,"canary")

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# Create a text/plain message
msg = MIMEText(sys.argv[1])

msg['Subject'] = 'ALERT: Usage beyond threshold'
msg['From'] = "alert-devops@gmail.com"
msg['To'] = config['gmail_user']

s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(config['gmail_user'],config['gmail_passwd'])
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()


