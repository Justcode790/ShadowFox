```
# 📊 Python Visualization with Matplotlib & Pandas

This project demonstrates how to create a variety of data visualizations using two powerful Python libraries: **Matplotlib** and **Pandas**.



---

## 📌 Library Overview

### Matplotlib

Matplotlib is a foundational Python library for creating **static**, **animated**, and **interactive** visualizations. It offers detailed control for publication-quality graphics and complex custom visualizations.

#### ✅ Use Cases:
- Scientific and engineering plots
- Custom and detailed visualizations
- Embedding plots in GUIs or web apps

#### 🔧 Installation:

```bash
pip install matplotlib
pip install numpy
```

---

## 📈 Graph Types in Matplotlib

### 1. Line Graph

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker='o', color='teal', linewidth=2)
plt.xlabel('Time (days)')
plt.ylabel('Value')
plt.title('Trend Over Time')
plt.grid(True)
plt.show()
```

---

### 2. Bar Chart

```python
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C']
values = [5, 7, 3]

plt.bar(categories, values, color='coral')
plt.title('Category Comparison')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()
```

---

### 3. Scatter Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.scatter(x, y, color='purple', s=100)
plt.title('Variable Relationship')
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.show()
```

---

### 4. Histogram

```python
import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4]

plt.hist(data, bins=4, color='skyblue', edgecolor='black')
plt.title('Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

---

### 5. Pie Chart

```python
import matplotlib.pyplot as plt

sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Proportional Distribution')
plt.axis('equal')
plt.show()
```

---

## 🐼 Visualizing with Pandas

Pandas provides built-in plotting functions that use Matplotlib behind the scenes for **quick and clean visualizations**.

```bash
pip install pandas
```

### Sample DataFrame:

```python
import pandas as pd

df = pd.DataFrame({
    'Year': [2017, 2018, 2019, 2020],
    'Sales': [200, 250, 300, 350]
})
```

---

### 1. Line Plot

```python
df.plot(x='Year', y='Sales', kind='line', marker='o', title='Sales Trend')
plt.show()
```

---

### 2. Bar Chart

```python
df.plot(x='Year', y='Sales', kind='bar', color='orange', title='Annual Sales')
plt.show()
```

---

### 3. Scatter Plot

```python
df.plot.scatter(x='Year', y='Sales', color='green', title='Year vs Sales')
plt.show()
```

---

### 4. Histogram

```python
df['Sales'].plot(kind='hist', bins=4, color='purple', title='Sales Distribution')
plt.show()
```

---

### 5. Pie Chart

```python
df['Sales'].plot(kind='pie', labels=df['Year'], autopct='%1.1f%%', title='Sales Share by Year')
plt.show()
```

---

## ⚖️ Comparison

| Feature        | Matplotlib                        | Pandas                              |
|----------------|-----------------------------------|-------------------------------------|
| Ease of Use    | Flexible but setup-intensive      | One-liner from DataFrame/Series     |
| Customization  | Full control                      | Basic customization only            |
| Interactivity  | Supports animations & interaction | Minimal (relies on Matplotlib)      |
| Performance    | Great for complex datasets        | Fast for moderate datasets          |
| Best For       | Publication-quality visuals       | Fast EDA and quick insights         |
| Integration    | GUIs, web apps                    | Seamless with data manipulation     |

---

## 🧠 Summary

- **Matplotlib**: Best for customized, high-quality visualizations.
- **Pandas**: Ideal for quick, in-line visualizations during analysis.

They are often **used together**:  
**Pandas** for quick exploration and **Matplotlib** for final refinement.

---

## 🖼️ Screenshots (Optional)



## ✅ Author

Thank you
```
