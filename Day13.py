import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
STUDENT = [45,55,75,80,67,90]
df = pd.DataFrame({"Marks":STUDENT})
sns.histplot(df["Marks"],kde = True,color = "cyan")
plt.title("DISTRIBUTION OF STUDENT MARKS")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

print("skewness:",df["Marks"].skew())