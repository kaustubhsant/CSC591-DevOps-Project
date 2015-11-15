#!/bin/bash

while true;do
free -m >> usage.logs
df -h $HOME >>usage.logs
diskuse=$(tail -1 usage.logs|awk '{print $5; }'|cut -d'%' -f1)
if [ $diskuse -gt 70 ]; then
	python sendmail.py "Disk usage: ${diskuse}% exceeds threshold 70%"  
	echo "Disk usage exceeded"
fi
usedmem=$(tail -5 usage.logs|head -1|awk '{print $3; }')
totalmem=$(tail -5 usage.logs|head -1|awk '{print $2; }')
pertmem=$(echo "scale = 2; $usedmem/$totalmem"|bc)
if [ ${pertmem#.*} -gt 50 ]; then
	python sendmail.py "Memory usage: ${pertmem}% exceeds threshold 50%"  	
	echo "Memory usage exceeded"
fi
sleep 2
done
