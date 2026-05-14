import pandas as pd
data = {"NAME":["AMIT","RIYA","JOHN","ROHIT"],"AGE" : [25,30,35,22],"SALARY":[50000,40000,60000,55000]}
df = pd.DataFrame(data)
print("Original dataset\n",df)

#filter
filtered = df[(df["SALARY"] > 50000) & (df["AGE"] < 30)]
print("filtered dataset\n",filtered)

#save filtered data to new file
filtered.to_csv("filtered.csv",index = False)