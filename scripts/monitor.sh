#!/bin/bash

free -m >> usage.logs
df -h $HOME >>usage.logs
diskuse=$(tail -1 usage.logs|awk '{print $5; }'|cut -d'%' -f1)
if [ $diskuse -gt 70 ]; then
	python sendmail.py "Disk usage: ${diskuse} exceeds threshold"  
	echo "Disk usage exceeded"
fi
usedmem=$(tail -5 usage.logs|head -1|awk '{print $3; }')
totalmem=$(tail -5 usage.logs|head -1|awk '{print $2; }')
pertmem=$(echo "scale = 2; $usedmem/$totalmem"|bc)
echo ${pertmem}
if [ ${pertmem#.*} -gt 60 ]; then
	python sendmail.py "Memory usage: ${pertmem}% exceeds threshold"  	
	echo "Memory usage exceeded"
fi
