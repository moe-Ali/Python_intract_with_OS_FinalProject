#!/usr/bin/env python3
import re
import operator
import csv
import sys

args=sys.argv
if len(args) >2:
    print("!Error! Number of arguments Must not be more than 1")
    exit()
elif len(args)==2:
    logfile=args[1]
else:
    logfile="syslog.log"
    
dic_error={}
dic_user={}

with open(logfile,"r") as f:
    for line in f:
        line=line.strip()
        if re.search(r"ticky: INFO ([\w ]*) ", line):
            info=re.search(r"ticky: INFO (.*) \((.*)\)", line)
            #saving data in dic_user
            if info.group(2) in dic_user.keys():
                dic_user[info.group(2)][0]+=1
            else:
                dic_user[info.group(2)]=[1,0]
                
        elif re.search(r"ticky: ERROR ([\w ]*) ", line):
            error=re.search(r"ticky: ERROR (.*) \((.*)\)", line)
        
            # saving data in dic_error 
            if error.group(1) in dic_error.keys():
                dic_error[error.group(1)]+=1
            else:
                dic_error[error.group(1)]=1
            
            #saving data in dic_user
            if error.group(2) in dic_user.keys():
                dic_user[error.group(2)][1]+=1
            else:
                dic_user[error.group(2)]=[0,1]
                
        else:
            continue
        
#sorting the dic_error by number of errors from most common to least common
sortdic_error=sorted(dic_error.items(), key=operator.itemgetter(1),reverse=True)
sortdic_error.insert(0,("Error", "Count"))

#sorting the dic_user by username
sortdic_user=sorted(dic_user.items())
sortdic_user.insert(0,("Username", "INFO", "ERROR"))

#making the desired output instade of ('Username', ['INFO','ERROR']) to ("Username", "INFO", "ERROR")
for i in range(len(sortdic_user)):
    if i == 0:
        continue
    else:
        sortdic_user[i]=(sortdic_user[i][0],sortdic_user[i][1][0],sortdic_user[i][1][1])
      
#saving the values in sortdic_error in error_message.csv 
with open("error_message.csv","w",newline="") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerows(sortdic_error)

#saving the values in sortdic_user in user_statistics.csv
with open("user_statistics.csv","w",newline="") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerows(sortdic_user)
    
