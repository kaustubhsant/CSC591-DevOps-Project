import boto.ec2
import time
from dateutil.parser import *
import os.path
import uuid
from time import sleep
import datetime
import smtplib
import json
from email.mime.text import MIMEText



with open("config/config.json",'r') as cfg:
	config = json.load(cfg)

msg = "Instance is expired and it need to be rebooted"

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

print "--------------Check 3 : Scanning for expired instances-------------"

reservations = conn.get_all_reservations()

for r in reservations:
	for instance in r.instances:
		#print instance.state
		if instance.state == 'running':
			#print instance.launch_time
			lt_datetime = parse(instance.launch_time)
			lt_delta = datetime.datetime.now(lt_datetime.tzinfo) - lt_datetime
			uptime = str(lt_delta)
	        #print(uptime)
			timelist = uptime.split(":")
			#print timelist
			if timelist[0] >= '0':
				print "******Instance" + instance.id + "is expired and it need to be rebooted....*******"
				print "       Reporting Instance id : " + instance.id+ "        "
				print "       Reporting Instance ip : " + instance.ip_address+ "      "
				s.sendmail(msg['From'], msg['To'], msg.as_string())
			elif timelist[0] == '1' and (timelist[1] > '0' or timelist[2] > '0'):
				print "******Instance" + instance.id + "is expired and it need to be rebooted....*******"
				print "       Reporting Instance id : " + instance.id+ "        "
				print "       Reporting Instance ip : " + instance.ip_address+ "      " 
				s.sendmail(msg['From'], msg['To'], msg.as_string())


s.quit()


