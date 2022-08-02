import numpy,pandas
'''1.INTODUCTION AND BASICS
To upload csv file to pyyhon
df=pandas.read_csv("file location")

load from python to csv file
df.to_csv ("location of file")

to upload xlsx exel file in python
df=pandas.read_excel("file location")

to load from python to .xlsx file
df.to_excel("file location")'''
df=pandas.read_csv('E:\learn\machine learning\Lesson 3 Practice\mtcars.csv',delimiter=',')#loading file into variable df
# importing as numpy array
model=numpy.array(df['model'])
print (df)#prints whole datasets
print(model)#prints only models column






