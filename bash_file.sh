#!/bin/bash

#Given a text file file.txt that contains a list of phone numbers (one per line),
#write a one-liner bash script to print all valid phone numbers.
#
#You may assume that a valid phone number must appear in one of the following two formats:
#(xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
#
#You may also assume each line in the text file must not contain leading or trailing white spaces.
#

######################################################  FIRST SOLUTION

#
#reg1="^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$"
#reg2="^[0-9]{3}-[0-9]{3}-[0-9]{4}$"
#
#while read
#do
#    if [[ $REPLY =~ $reg1 || $REPLY =~ $reg2 ]]
#    then
#     echo $REPLY
#    fi
#done<file.txt

#second solution
cat file.txt | awk '/^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$/{print $0}'





#read var1 var2
#
#echo "var1  $var1"
#
#echo "var2  $var2"
#

#cnt=0
#
#((cnt+=100))
#echo $cnt
#

#
#cnt=5
#if [ $cnt -gt 4 ] && [ $cnt -lt 10 ]
#then
#echo 'kkkk'
#fi

##
#file=fl1.txt


#while read line
#do
#
#  if [ $line =~ ^\([0-9]{3}\)[[:blank:]][0-9]{3}\-[0-9]{4} ] or [ $line =~ [0-9]{3}\-[0-9]{3}\-[0-9]{4} ]
#  then
#  echo $line
#  fi
#
#done <$file

#
#awk 'NR==10 {print}' file.txt
#sed -n '10p' file.txt