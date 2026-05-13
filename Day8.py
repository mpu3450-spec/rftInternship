import pandas as pd
data = {"NAME":["A","B","C","D"],"DEPT":["IT","HR","IT","HR"],"SALARY":[50000,40000,60000,45000]}
df = pd.DataFrame(data)

#Find average salary per department
avg = df.groupby("DEPT")["SALARY"].mean()
print(avg)

#highest paid employee per department
print("highest paid employee",df.loc[df.groupby("DEPT")["SALARY"].idxmax()])

#count employees per department
print(df.groupby("DEPT")["NAME"].count())

#sort department by average salary
print(avg.sort_values(ascending = False))