import matplotlib.pyplot as plt
import numpy as np
STUDENTS = ["AMIT","RIYA","JOHN"]
SUBJECTS = ["Math","Science","English"]
amit_marks = [85,78,90]
riya_marks = [92,88,85]
john_marks = [78,82,74]

#Grouped bar chart
x = np.arange(len(SUBJECTS))
width = 0.25

plt.bar(x-width , amit_marks,width,label = "Amit",color = "red")
plt.bar(x, amit_marks,width,label = "Riya",color = "blue")
plt.bar(x+width,john_marks,width,label = "John",color ="green")
plt.xlabel("STUDENTS")
plt.ylabel("MARKS")
plt.title("STUDENT PERFORMANCE")
plt.xticks(x,SUBJECTS)
plt.legend()
plt.show()