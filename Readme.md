#Team

ksant, abambre, vsnarvek

#Deployment


###Goal 4
**_The ability to monitor the deployed application (using at least 2 metrics) and send alerts using email or SMS (e.g., smtp, mandrill, twilio). An alert can be sent based on some predefined rule._**

The [monitor.sh](scripts/monitor.sh) and [sendmail.py](scripts/sendmail.py) code completes this goal.
The [monitor.sh](scripts/monitor.sh) checks the disk usage and memory usage and logs them every 2 seconds. If the disk usage exceeds set threshold of 70% or memory usage exceeds 50%, an email alert is sent. It also removes the corresponding entry for *canary* from the global redis store so that the proxy server will stop all traffic to this canary release. 

![image](images/alert.png)
