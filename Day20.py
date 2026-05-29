import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")

#Data cleaning
print(df.isnull().sum())
df.drop(columns = "Region_and_Sales_Rep",inplace=True)
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])
print(df)

#Analysis
print(df.info())

#Total Sales
print("total sales:",df["Sales_Amount"].sum())

#sales per region
print(df.groupby("Region")["Sales_Amount"].sum())

#top sold category
top_sold = df.groupby("Product_Category")["Sales_Amount"].sum()
print("Top sold Category:",top_sold.idxmax())

#Visualization
plt.figure(figsize=(10,5))
# Pie Chart
plt.subplot(1,2,1)
top_sold.plot(kind = "pie",autopct = "%1.1f%%",)
plt.title("Top Sold Products")
# Bar Chart
plt.subplot(1,2,2)
region_based =df.groupby("Region")["Sales_Amount"].sum()
region_based.plot(kind = "bar")
plt.title("SALES AMOUNT")
plt.xlabel("region")
plt.ylabel("sales_amount")
plt.tight_layout()
plt.show()

print("INSIGHTS")
print("Category clothing has highest sales")
print("North region has highest sales")
print("South is the least sales region")
print("food is least sold category")