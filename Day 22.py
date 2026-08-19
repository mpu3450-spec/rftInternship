import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Order_ID": [
        "O001", "O002", "O003", "O004", "O005",
        "O006", "O007", "O008", "O009", "O010",
        "O011", "O012", "O013", "O014", "O015",
        "O015"
    ],

    "Date": [
        "2026-08-01", "2026-08-02", "2026-08-03", "2026-08-04",
        "2026-08-05", "2026-08-06", "2026-08-07", "2026-08-08",
        "2026-08-09", "2026-08-10", "2026-08-11", "2026-08-12",
        "2026-08-13", "2026-08-14", "2026-08-15", "2026-08-15"
    ],

    "Customer": [
        "Rahul", "Priya", "Aman", "Neha", "Rahul",
        "Riya", "Aman", "Karan", "Priya", "Rahul",
        "Neha", "Karan", "Riya", "Aman", "Priya", "Priya"
    ],

    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor", "Laptop",
        "Headphones", "Mouse", "Keyboard", "Monitor", "Laptop",
        "Headphones", "Laptop", "Mouse", "Monitor", "Keyboard", "Keyboard"
    ],

    "Category": [
        "Electronics", "Accessories", "Accessories", "Electronics",
        "Electronics", "Accessories", "Accessories", "Accessories",
        "Electronics", "Electronics", "Accessories", "Electronics",
        "Accessories", "Electronics", "Accessories", "Accessories"
    ],

    "Quantity": [
        1, 2, 1, 1, 1,
        2, 3, 2, 1, 1,
        2, 1, 4, 1, 2, 2
    ],

    "Sales": [
        55000, 1600, 2500, 18000, 55000,
        5000, None, 5000, 18000, 55000,
        5000, 55000, None, 18000, 5000, 5000
    ]
}

df = pd.DataFrame(data)
df.to_csv("Sales.csv")

#handle missing values
print(df.isnull().sum())
df["Sales"]= df["Sales"].fillna(df["Sales"].mean())
print(df)

#finding duplicate values
print(df.duplicated().sum())

#total sales
print("total sales",df["Sales"].sum())

#average revenue
avg_revenue = df['Sales'].mean()
print("average revenue" ,avg_revenue)

#top 5 customers
top = df.groupby("Customer")["Sales"].sum()
top_5 = top.sort_values(ascending=False)
print(top_5)

#using date time
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["Sales"].sum()

#line chart
plt.plot(daily_sales.index , daily_sales.values)
plt.xlabel("date")
plt.ylabel("sales")
plt.xticks(rotation = 45)
plt.show()

#bar chart
top_products = df.groupby("Product")["Sales"].sum()

#bar plot
plt.bar(top_products.index , top_products.values)
plt.xlabel("products")
plt.ylabel("Sales")
plt.show()

#pie chart
category_group = df.groupby("Category")["Sales"].sum()
plt.pie(category_group.values,labels=category_group.index, autopct = "%1.1f%%")
plt.legend()
plt.show()
print("Business Insights")
print("Laptop is the top-selling product because it generates the highest total sales compared to other products.")
print("Electronics is the highest-revenue category, mainly because products like laptops and monitors have higher selling prices.")
print("Rahul is the top customer based on total sales, making Rahul a valuable customer for the business.")
print("Sales fluctuate across different dates, with some days generating significantly higher sales than others, mainly due to laptop purchases.")
print("Accessories have more product variety and quantity sold, but Electronics contributes more to total revenue because of its higher-priced products.")