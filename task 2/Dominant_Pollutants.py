import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('delhiaqi.csv', parse_dates=['date'], index_col='date') 
daily_avg = df[['pm2_5', 'pm10', 'co', 'no2', 'nh3']].resample('D').mean() 


plt.figure(figsize=(12,6)) 
daily_avg.plot(marker='o') 
plt.title('Daily Average Concentration of Major Pollutants (Jan 1-10, 2023)') 
plt.ylabel('Concentration (μg/m³)')
plt.xlabel('Date') 
plt.xticks(rotation=45, ha='right') 
plt.axhline(60, color='r', linestyle='--', label='PM2.5 NAAQS') 
plt.axhline(100, color='g', linestyle='--', label='PM10 NAAQS') 
plt.legend() 
plt.tight_layout() 
plt.show() 