import matplotlib.pyplot as plt 
 
sizes = [15, 30, 45, 10] 
labels = ['A', 'B', 'C', 'D'] 
 
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140) 
plt.title('Proportional Distribution') 
plt.axis('equal') 
plt.show() 