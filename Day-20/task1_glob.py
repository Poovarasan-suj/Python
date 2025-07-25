import glob

logs = glob.glob ("/home/sujith/Python/logs/*.log") 

# Using glob to find all .log files in the specified directory
print("Log files found:")
for log in logs:
    print(log)
print("Total number of log files:", len(logs))
print("End of log file search.")


