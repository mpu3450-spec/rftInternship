#SALLES DATA ANALYZER
import pandas as pd
df = pd.read_csv("Sales.csv")
#Add new column
df["TOTAL"] = df["QUANTITY"]*df["PRICE"]
#total sales per product
sales_per_product = df.groupby("PRODUCT")["TOTAL"].sum()
print("total sales per product:",sales_per_product)
#total revenue
print("TOTAL REVENUE:",sum(df["TOTAL"]))
#top selling product
print("TOP SELLING PRODUCT",sales_per_product.idxmax())
#sort
print(df.sort_values("TOTAL"))