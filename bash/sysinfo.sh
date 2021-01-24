#!/bin/bash
#Create a script that emails us our user, IP, hostname
#Displays today's date

emailaddress=juilfsjc@mail.uc.edu
today=$(date +"%d-%m-%Y %H:%M:%S")
ip=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
hostname=$(hostname | grep 'juilfsjc.centos')
content="User: $USER

Server name is: $hostname

IP address is: $ip

Date and time is: $today"

echo "Email will contain: $content"
mail -s "IT3038C Linux IP" $emailaddress <<< $(echo -e $content)
