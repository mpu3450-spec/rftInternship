import pandas as pd
data = {"NAME" :["AMIT","RIYA","JOHN"],"MATH" : [80,90,60],"SCIENCE":[70,88,65],"ENGLISH" : [85 ,92,70]}
df = pd.DataFrame(data)

#calculate average marks per student
df['AVERAGE'] = (df["MATH"] + df['SCIENCE'] + df['ENGLISH'])/3
avg = df.groupby("NAME")["AVERAGE"].mean()
print(avg)

#TOPPER
print("TOPPER:",avg.idxmax())

#count students above average
overall = avg.mean()
print("number of students above average:",len(df[df["AVERAGE"] > overall]))

#Add grade column
def grade(avg):
    if avg > 90:
        return "A"
    elif avg > 80:
        return "B"
    elif avg > 70:
        return "C"
    elif avg > 60:
        return "D"
    else:
        return "FAIL"
    
df["GRADE"] =df["AVERAGE"].apply(grade)
print(df)    

#subject wise average
print("average marks of maths:",df["MATH"].mean())
print("average marks of science:",df["SCIENCE"].mean())
print("average marks of english:",df["ENGLISH"].mean())