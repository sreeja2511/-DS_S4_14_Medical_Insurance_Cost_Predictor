import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

# Bar chart
height = [10,24,36,40,5]
names = ['one','two','three','four','five']
colors = ['red','green','blue','orange','purple']
plt.bar(names,height,width=0.8,color=colors)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My bar chart!')
plt.show()

# Subplots with iris data
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

plt.figure(figsize=(12, 8))
plt.subplot(2,3,1)
plt.plot(df['sepal length (cm)'],df['sepal width (cm)'])
plt.subplot(2,3,2)
plt.plot(df['petal length (cm)'],df['petal width (cm)'])
plt.subplot(2,3,3)
plt.scatter(df['sepal length (cm)'],df['sepal width (cm)'])
plt.title('subplots')
plt.show()