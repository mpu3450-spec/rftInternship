#Aimple Log Analyzer
logs = ["ERROR DISK FULL","INFO STARTED","ERROR FILE MISSING","WARNING MEMORY LOW"]

#Dictionary to store counts
count = { "ERROR":0,"INFO":0,"WARNING":0}

#Analyze logs
for log in logs:
    log = log.upper()

    if "ERROR" in log:
        count["ERROR"] += 1
    elif "INFO" in log:
        count["INFO"] += 1
    else:
        count["WARNING"] += 1
print(count)

total = 0
for key,value in count.items():
    if value > total:
        total = value
        print("most frequent log type:",key," ",value)