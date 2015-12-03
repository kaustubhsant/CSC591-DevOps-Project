#!/bin/bash


white_listed_ports="22 80"

while true;do


echo "----------Conformity Check begins---------------"
echo "         Check 1 : Scanning for unwanted open ports "


	while read input
	do
    	echo "                  Checking instance : $input"

		nc -zv "$input" 1-40  > conformity.log 2>&1

		grep "succeeded*" conformity.log | cut -d ' ' -f 4 | while read -r line ; do
		  #echo "Processing $line"

		if echo "$white_listed_ports" |grep -q "$line";then
			#Ignore ports 
			echo 
		else
			echo "******** Conformity Check violation***********"
			echo "******** Only following ports are allowed to be open : < $white_listed_ports >***********"
			echo "Violation : Port $line is opened for connections"
			echo "Terminating instance $input..."
			python stop.py $input
			echo "Instance $input is Terminated"
		fi

		done

	done <instance_list.txt

sleep 2

done