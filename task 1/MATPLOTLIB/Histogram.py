import matplotlib.pyplot as plt 
 
data = [1, 2, 2, 3, 3, 3, 4] 
 
plt.hist(data, bins=4, color='skyblue', edgecolor='black') 
plt.title('Data Distribution') 
plt.xlabel('Value') 
plt.ylabel('Frequency') 
plt.show()