MARKS = [78,85,90,67,85,92,78]
#average
sum = 0
for i in range(0,len(MARKS)):
    sum += MARKS[i]
avg = sum/len(MARKS)    
print("Average:",avg)

#Highest
max = MARKS[0]
for i in range(0,len(MARKS)):
    if(MARKS[i] > max):
        max = MARKS[i]
print("MAXIMUM element:",max)

#Lowest
min = MARKS[0]        
for i in range(0,len(MARKS)):
    if(MARKS[i] < min):
        min = MARKS[i]        
print("MINIMUM element:",min)

#students scoring above average
count = 0
for i in range(0,len(MARKS)):
    if(MARKS[i] > avg):
        count += 1
print("number of students scoring marks above average:",count)

#grade distribution
def grade_distribution(m):
        if( m > 80):
             return "A"
        elif(m > 60):
             return "B"
        elif(m > 40):
            return "C"  
        else:
            return "FAIL"

print("grades are as followed:")
for i in range(len(MARKS)):
          print(grade_distribution(MARKS[i]))      
       