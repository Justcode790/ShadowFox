import pandas as pd 
import matplotlib.pyplot as plt   
 
df = pd.DataFrame({ 
    'Year': [2017, 2018, 2019, 2020], 
    'Sales': [200, 250, 300, 350] 
}) 
 
df.plot(x='Year', y='Sales', kind='bar', color='orange', title='Annual Sales') 
 
plt.show() 