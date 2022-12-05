#!/bin/bash

#read var1 var2
#
#echo "var1  $var1"
#
#echo "var2  $var2"
#


cnt=0

((cnt+=100))
echo $cnt




#
#file=fl1.txt
#cnt=0
#
#while read -r line
#do
#  ((cnt+=101))
#  if [ $cnt -gt 100 ]
#  then
#  echo $line
#  fi
#done <$file

#
#awk 'NR==10 {print}' file.txt
#sed -n '10p' file.txt