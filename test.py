import seaborn
import pandas as pd


seaborn.set(style='whitegrid')
df1=pd.read_csv('E:\learn\machine learning\Lesson 3 Practice\mtcars.csv')

seaborn.boxplot(x="disp",y="hp",data=df1)

