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
#
##second solution
#cat file.txt | awk '/^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$/{print $0}'
#

#
#Write a bash script to calculate the
#frequency
# of each word in a text file words.txt.
#
#For simplicity sake, you may assume:
#
#words.txt contains only lowercase characters and space ' ' characters.
#Each word must consist of lowercase characters only.
#Words are separated by one or more whitespace characters.
#Example:
#
#Assume that words.txt has the following content:
#
#the day is sunny the the
#the sunny is is
#Your script should output the following, sorted by descending frequency:
#
#the 4
#is 3
#sunny 2
#day 1
#

file=fl1.txt
declare -A array

while read line
do
     for word in $line
     do
       if [ -n "${array[$word]}" ]
       then
          array["$word"]=$((${array["$word"]} + 1))
       else
         array["$word"]=1
       fi
     done
done < $file

for key in "${!array[@]}"
do
echo $key ${array[$key]}
done | sort -k2 -rn
