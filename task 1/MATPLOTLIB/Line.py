import matplotlib.pyplot as plt 
 
x = [1, 2, 3, 4] 
y = [10, 20, 25, 30] 
 
plt.plot(x, y, marker='o', color='teal', linewidth=2) 
plt.xlabel('Time (days)') 
plt.ylabel('Value') 
plt.title('Trend Over Time') 
plt.grid(True) 
plt.show() 