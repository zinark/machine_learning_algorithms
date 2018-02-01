import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)

df = pd.read_csv("iris.data", names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
print df.head()

iris = sns.load_dataset("iris")
print iris.describe()
print iris.info()
print iris["species"].value_counts()

iris.hist(edgecolor='black', linewidth=1.2, figsize=(16, 12))
plt.show()

sns.pairplot(iris, hue='species', size=2, aspect=1)
#pd.scatter_matrix(iris, figsize=(16,12))
plt.show()

plt.figure(figsize=(26,12))
plt.subplot(2,2,1); sns.violinplot(x='species', y='sepal_length',data=iris)
plt.subplot(2,2,2); sns.violinplot(x='species', y='sepal_width',data=iris)
plt.subplot(2,2,3); sns.violinplot(x='species', y='petal_length',data=iris)
plt.subplot(2,2,4); sns.violinplot(x='species', y='petal_width',data=iris)
plt.show()

