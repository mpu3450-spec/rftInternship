l = []
with open("file.csv","r") as f:
    data = f.read()
    print(data)

with open("file.csv","r") as f:
    header = f.readline().strip().split(",")
    for line in f:
        values = line.strip().split(",")
        d = {}
        for i in range(len(header)): 
          key = header[i]
          value = values[i]
          if value.isdigit():
              d[key] = int(value)
          else:
              d[key] = value
        l.append(d)          
print(l)
total = 0
for s in l:
    total += s["MARKS"]
average = total/len(s) 
print("Average Marks=",average)   


       