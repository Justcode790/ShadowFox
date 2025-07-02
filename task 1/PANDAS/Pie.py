import pandas as pd 
import matplotlib.pyplot as plt   
 
df = pd.DataFrame({ 
    'Year': [2017, 2018, 2019, 2020], 
    'Sales': [200, 250, 300, 350] 
}) 
 
df['Sales'].plot(kind='pie', labels=df['Year'], autopct='%1.1f%%', title='Sales Share by Year') 
 
plt.show() 