'''6.DATA MANIPULATION
head() is used to return data of first n rows
print(df.head(n))


tail() is used to return data of last n rows
print(df.tail(n))

values is used to return  actual data in series of array
print(df.values)

group by is used to group data acc to given condition
print(df.groupby(['col1','col2']).groups)

concatenation
it is used to combine two or more data structure*add whole data
print(pandas.concat([df1,df2],axis=1))#combine two data structure df1 and df2
merging
Merging is the Pandas operation that performs database joins on objects *adds column on basis of common object
print(pandas.merge(df1,df2,on='common object of both datas'))

Joins are used to combine records from two or more tables in a database. Below 
are the four most commonly used joins:
1.Left join=Returns all rows from  the left table, even if  there are no matches in  the right table
print(pandas.merge(df1,df2,on='common object of both datas',how='left'))
2.Right join=Preserves the unmatched  rows from the second  (right) table, joining them  with a NULL in the shape  of the first (left) table
print(pandas.merge(df1,df2,on='common object of both datas',how='right'))
3.Inner join=Selects all rows from  both participating tables  if there is a match between columns
print(pandas.merge(df1,df2,on='common object of both datas',how='inner'))
4.Full outer join=Returns all records when  there is a match in either  left (table1) or right  (table2) table records
print(pandas.merge(df1,df2,on='common object of both datas',how='outer'))



'''
import numpy as np
import pandas as pd
df=pd.read_csv('E:\learn\machine learning\Lesson 3 Practice\mtcars.csv',delimiter=',')
print(df.head(6))#returning first 6 rows of data
print(df.tail(5))#returning last 5 rows of data
print(df.values)#return actual data in form of series of array
print(df.groupby(['hp','disp']).groups)#group data of two column hp and disp
