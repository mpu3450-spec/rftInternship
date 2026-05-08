l = []
with open("file.csv","r") as f:
    data = f.read()
    print(data)

with open("file.csv","r") as f:
    header = f.readline().strip().split(",")
    for line in f:
        value = line.strip().split(",")
        d = {}
        for i in range(len(header)): 
          d[header[i]] = int(value[i]) if value[i].isdigit() else value[i]
        l.append(d)

print(l)



       