import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = pd.read_csv('delhiaqi.csv', parse_dates=['date'], index_col='date') 
df['hour'] = df.index.hour 
hourly_avg = df.groupby('hour')[['pm2_5', 'pm10']].mean() 
plt.figure(figsize=(10,5)) 
hourly_avg.plot(marker='o') 
plt.title('Average Hourly PM2.5 and PM10 Concentration') 
plt.ylabel('Concentration (μg/m³)') 
plt.xlabel('Hour of Day') 
plt.xticks(range(0,24)) 
plt.grid(True) 
plt.tight_layout() 
plt.show()