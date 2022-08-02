
'''5.OUTLIER AND its TREATMENT
outlier are data that have very out range from other data
import seaborn as sns
sns.boxplot(x=df1['column name'])

filter=df1['column name'].values>60
df1_outlier_rem=df1[filter]
df1_outlier_rem

filter is assigned to object then object is removed to remove outlier'''
import numpy as np,pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df1=pd.read_csv('E:\learn\machine learning\Lesson 3 Practice\mtcars.csv')
data=sns.boxplot(x=df1['hp'])#detecting outlier or visualising outlier
plt.show()
#removing the outlier ie value greater than 250 as seen in graph
filter = df1['hp']<250
df1_out_rem = df1[filter]
sns.boxplot(x=df1_out_rem['hp'])
plt.show()