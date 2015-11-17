#!/bin/bash

echo "After the Build is completed successfully"
echo "After the Test analysis and coverage stage completed successfully"

export abc=`ssh -oStrictHostKeyChecking=no -i /tmp/id_rsa root@104.131.206.44  "docker ps|grep 'prod_server' |wc -l"`

if [ "$abc" -eq "1" ]
then
	ssh -oStrictHostKeyChecking=no -i /tmp/id_rsa root@104.131.206.44  "docker stop prod_server;docker rm prod_server;docker rmi vsnarvek/milestone3"
fi

ssh -oStrictHostKeyChecking=no -i /tmp/id_rsa root@104.131.206.44  "docker run --name prod_server -d -p 8081:8000 vsnarvek/milestone3"

if [ "$?" != "0" ]; then
echo "Error"
  exit -1
fi
