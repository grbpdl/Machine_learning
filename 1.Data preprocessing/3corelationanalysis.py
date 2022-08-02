import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''
correlations = df.corr()
sns.heatmap(data = correlations,square = True, cmap = "bwr")#data->Rectangular dataset (2D dataset that can be coerced into an ndarray square->f True, set the Axes aspect to “equal” so each cell will be square-shaped //cmap->Matplotlib colormap name or object, or list of colors
Below is the code for plotting a heatmap within Python:

plt.yticks(rotation=0)
plt.xticks(rotation=90)'''
df=pd.read_csv('E:\learn\machine learning\Lesson 3 Practice\mtcars.csv')

correlations = df.corr()
sns.heatmap(data = correlations,square = True, cmap = "bwr")
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()


# print(df.describe())#shows the statical data for all attribute
# group=df[['mpg','cyl']].groupby(['mpg']).describe().unstack()#here we are extracting variables and grouping one wrt other unstack is used to display data in other way column as rows
# print(group)
# corelation=df[['model','hp']].corr()#this gives corelation between the variables
# print(corelation)
