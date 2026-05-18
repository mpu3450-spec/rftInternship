import pandas as pd
import matplotlib.pyplot as plt
DATES = ["MON","TUE","WED","THU","FRI"]
SALES = [200,250,300,280,350]
#line chart sahowing sales trend
plt.plot(DATES,SALES,marker = 'o')
plt.plot(DATES[SALES.index(max(SALES))],max(SALES),marker = 'o',color = "green")
plt.plot(DATES[SALES.index(min(SALES))],min(SALES),marker = 'o',color = "red")
plt.xlabel("DATES")
plt.ylabel("SALES")
plt.title("SALES TREND")
plt.show()