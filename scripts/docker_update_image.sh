#!/bin/bash

sudo docker build -t milestone3 .


docker run --name demo -d -p 8081:8000 milestone3

docker tag -f milestone3 vsnarvek/milestone3:latest

docker push vsnarvek/milestone3:latest

