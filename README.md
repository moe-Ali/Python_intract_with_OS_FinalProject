# Python_intract_with_OS_FinalProject
### This is my final project at Coursera Using Python to Interact with the Operating System by Google

## which converts the syslog file into 2 CSV files:
  - error_message.csv contains The ranking of errors generated by the system: A list of all the error messages logged and how many times each error was found, sorted by the most common error to the least common error.
  - user_statistics.csv contains The user usage statistics for the service: A list of all users that have used the system, including how many info messages and how many error messages they've generated. This report is sorted by username.
  
## To run the script use:
```
chmod +x final.py
./final.py
```
or specify syslog file location
```
chmod +x final.py
./final.py {syslog file path}
```
