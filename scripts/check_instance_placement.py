import boto.ec2
import time
import os.path
import uuid
from time import sleep
import smtplib
import json
from email.mime.text import MIMEText

print "--------------Check 2 : Verfying placement of the instances-------------"


with open("config/config.json",'r') as cfg:
	config = json.load(cfg)

msg = "Incorrect placement for instance"

msg['Subject'] = 'ALERT: Incorrect placement for instance'
msg['From'] = "alert-devops@gmail.com"
msg['To'] = config['gmail_user']

s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(config['gmail_user'],config['gmail_passwd'])

# Get connection object required for the operations
conn = boto.ec2.connect_to_region("us-west-2",
aws_access_key_id='',
aws_secret_access_key='')

reservations = conn.get_all_reservations()

# print reservations

# instances = reservations[0].instances
# print instances

# instance = instances[0]
# print instance

# print instance.placement

for r in reservations:
	for instance in r.instances:
		if instance.state == 'running':
			print instance
			if instance.placement != "us-west-2c":
				print "****** Incorrect placement for instance : " + instance.id
				print "       Instance is placed in following region :"+ instance.placement 
				print "****** Reporting Instance" + instance.id + "*********"
				s.sendmail(msg['From'], msg['To'], msg.as_string())
				#Sending mail 
				#print instance.ip_address

s.quit()

