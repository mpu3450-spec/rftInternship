import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "NAME": ["Riya", "Priya", "Rohit", "Amit", "Karan","Sneha","Rahul","Gunika"],
    "MARKS": [85, 92, 78, 88, 95,97,77,93]
}
df = pd.DataFrame(data)
fig = plt.figure(figsize=(15,5))

ax1 = fig.add_subplot(1,3,1)
sns.lineplot(x = df["NAME"],y = df["MARKS"],color = "pink",ax=ax1)
ax1.set_title("STUDENTS MARKS TREND")
ax1.set_xlabel("name")
ax1.set_ylabel("marks")

ax2 = fig.add_subplot(1,3,2)
ax2.bar(df["NAME"],df["MARKS"],color = "purple")
ax2.set_title("COMPARISON")
ax2.set_xlabel("name")
ax2.set_ylabel("marks")

ax3 = fig.add_subplot(1,3,3)
sns.histplot(df["MARKS"],kde = True,color = "cyan",ax=ax3)
ax3.set_title("MARKS DISTRIBUTION")
ax3.set_xlabel("marks")
ax3.set_ylabel("frequency")
plt.tight_layout()
plt.show()

print("INSIGHTS")
print("Sneha obtained highest marks")
print("Rohit obtained least marks")
print("most of the students obtained marks above 80")