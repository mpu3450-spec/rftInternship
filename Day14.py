#CATEGORY BREAKDOWN
import matplotlib.pyplot as plt
CATEGORIES = ["FOOD","TRAVEL","SHOPPING"]
EXPENSES = [500,300,200]
max = EXPENSES[0]
idx = 0
for i in range(len(EXPENSES)):
 if max <EXPENSES[i]:
  max = EXPENSES[i]
  idx = i
myexplode = []
color = []
for i in range(len(EXPENSES)):
 if i == idx:
  myexplode.append(0.2)
  color.append("cyan")
 else:
  myexplode.append(0)
  color.append("purple")
plt.pie(EXPENSES,labels = CATEGORIES,autopct = "%1.1f%%",explode = myexplode,colors = color,shadow = True)
plt.title("CATEGORIES",loc = "left")
plt.show()
