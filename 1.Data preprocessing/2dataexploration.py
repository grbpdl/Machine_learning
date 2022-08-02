import numpy,pandas
'''2.DATA EXPLORATION
to check dimension of data 
df.shape
it return a tuple (343,456) which represent row and column

to check data type
type(df)

to check data type of a column
df['columnname'].dtype

making list
list=[d1,d2,d3,..]
slicing list
list[startindex:end:step]

to perform slicing on data use
df.iloc[a:b,x:y] where a=start index of row b=end index of row x=start index of col y=endindex of row

to return unique data from column
df['columnname'].unique()

to return all data from column
df['columnname'].values()*

to return mean data 
df.mean()
df['column name'].mean() #for specefic column

to return median data 
df.median()

to return mode of data of column axis=0 and for row axis=1(mode also works for both numeric and non numeric data)
df.mode(axis=0)'''
df =pandas.read_csv('E:\learn\machine learning\Lesson 3 Practice\mtcars.csv',delimiter=',')
print(df)
# print (df.shape)#print dimension of data
# print(type(df))#print data type
# print(df['hp'].dtype)#print data type of a column
#list=[1,2,3,4,5]#defining a list in python
# print(list[1:4:2])#slicing a list by index value start:end:step
#we can also perform slicing on list data as
# slice=df.iloc[0:2,0:2]#slicing data as [row:row,col:col]
# print(slice)#printing sliced data
# print(df['hp'].unique())#printing unique data from column
#df['disp'].values()#return all data of a specefic column*
#mean  and median can only be applied in numeric values
# print(df.mean())#mean of all column
# print(df['hp'].mean())#to show mean of specefic column
# print(df.median())
#print(df.mode(axis=0))#axis 0 for column and 1 for row


