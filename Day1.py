data = [10,None,20,10,"",30,None,40]

#remove duplicates & remove invalid valued(None , empty string)
temp = []
for i in range(0,len(data)):
      if data[i] not in temp and data[i] != None and data[i] != "" :
         temp.append(data[i])

#clean & sorted list
print("list:",temp)

#count how many values are removed
values_removed = len(data) - len(temp)
print("values removed:",values_removed)

