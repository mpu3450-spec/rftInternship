import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Customer_ID": ["C101", "C102", "C103", "C104", "C105", "C106"],
    "Age": [22, 25, None, 28, 35, 40],
    "Spending": [1200, None, 2500, 2000, 3200, 4000],
    "Visits": [5, 8, 10, None, 12, 15]
}
df = pd.DataFrame(data)

#handle missing values
df["Age"]= df["Age"].fillna(df["Age"].mean())
df["Spending"]= df["Spending"].fillna(df["Spending"].mean())
df["Visits"]= df["Visits"].fillna(df["Visits"].mean())
print(df)

#group customer
group_customer = df.groupby("Customer_ID")["Spending"].sum()
print(group_customer)

#spending distribution
plt.figure(figsize = (6,4))
plt.hist(df["Spending"],bins = 5)
plt.title("Spending Distribution")
plt.xlabel("Spending")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#segments
def Category(Spending):
    if Spending >= 4000:
        return "high"
    elif Spending >= 2000:
        return "medium"
    else:
        return "low"
df["Category"]  = df["Spending"].apply(Category)  
 
 #high value customers
print(df[df["Category"] == "high"])  

#low engagement users
print(df[df["Visits"] < df["Visits"].mean()])  

#Customer Categories
segment = df["Category"].value_counts()
plt.bar(segment.index,segment.values)
plt.title("Customer Categories")
plt.xlabel("Category")
plt.ylabel("Number of customers")
plt.show()

# Business Strategies
print("\nBusiness Strategies:")
print("- Offer rewards to high-value customers")
print("- Send promotional offers to low-engagement users")
print("- Provide personalized recommendations")

