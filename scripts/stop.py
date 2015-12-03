import boto.ec2
import time
import os.path
import uuid
from time import sleep
import sys
import smtplib
import json
from email.mime.text import MIMEText

# Get connection object required for the operations
conn = boto.ec2.connect_to_region("us-west-2",
aws_access_key_id='',
aws_secret_access_key='')


with open("config/config.json",'r') as cfg:
	config = json.load(cfg)

msg = "Violation : Unauthorized opened Port for the connections"

msg['Subject'] = 'ALERT: Incorrect placement for instance'
msg['From'] = "alert-devops@gmail.com"
msg['To'] = config['gmail_user']

s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(config['gmail_user'],config['gmail_passwd'])


reservations = conn.get_all_reservations()

# print reservations

# instances = reservations[0].instances
# print instances

# instance = instances[0]
# print instance

# #conn.terminate_instances(instance_ids=
# state = instance.state
# print state

#instance.stop()


# state = instance.state
# print state

# while instance.state not in ('running', 'stopped'):
#     sleep(5)
#     instance.update()


for r in reservations:
	for instance in r.instances:
		if instance.state == 'running':
			if instance.ip_address == sys.argv[1]:
				instance.stop()
				while instance.state not in ('running', 'stopped'):
					sleep(5)
					instance.update()
				s.sendmail(msg['From'], msg['To'], msg.as_string())

s.quit()
