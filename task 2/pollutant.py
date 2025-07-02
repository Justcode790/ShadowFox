import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv('delhiaqi.csv', parse_dates=['date'], index_col='date')

pollutants = ['pm2_5', 'co', 'no2', 'nh3']
data = df[pollutants]

corr_matrix = data.corr(method='pearson')

print("Correlation matrix:")
print(corr_matrix)

for pollutant in ['co', 'no2', 'nh3']:
    r, p = pearsonr(data['pm2_5'].dropna(), data[pollutant].dropna())
    print(f"PM2.5 - {pollutant.upper()} correlation: r = {r:.2f}, p-value = {p:.4f}")

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Pollutants')
plt.show()
