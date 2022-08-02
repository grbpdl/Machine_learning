import numpy,pandas,sklearn
'''4.DATA WRANGLING(converting raw data into another format)

finding missing data if missing return true alse false
df.isna().any()
df.isna().sum()#to find no of missing data per column

treating missing data
for non numeric data
delete.dropna(axis=0,inplace=TRUE)#delete the missing observation ie row
delete.dropna(axis=1,inplace=TRUE)#delete complete column for missing data
df=df.fillna(df.mode().iloc[0])#replace with mode ie most repeating data

df.fillna(df.mean())#replace with mean
df.fillna(df.median())#replace with median
only for numeric values-to replace missing data with mean using sikit learn library 

from sklearn.impute import SimpleImputer
# Imputing with constant value; The command below replaces the missing
# value with constant value such as 80
#
imputer = SimpleImputer(missing_values=np.NaN, strategy='constant', fill_value=80)


mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
mean_imputer=mean_imputer.fit(df1)
imputed_df=mean_imputer.transform(df1.values)
df1=pd.DataFrame(data=imputed_df,columns=cols)

to replace missing data with median using sklearn
from sklearn.impute import SimpleImputer
median_imputer=SimpleImputer(missing_values=np.nan,strategy='median')
median_imputer=median_imputer.fit(df1)
imputed_df=median_imputer.transform(df1.values)
df1=pd.DataFrame(data=imputed_df,columns=cols)
'''

df1=pandas.read_csv('E:\learn\machine learning\Lesson 3 Practice\Salaries.csv',delimiter=',')
# print(df1.head())
# print(df1.isna().any())#find missing data
# print(df1.isna().sum())#find no of  data per column
#if there is any missing data then they can either be replaced by mean or median mode value or they can be deleted

# df1=df1.fillna(df1.mode().iloc[0])#replace with mode ie most repeating data mode
# print(df1.head())
# print(df1.isna().any())

from sklearn.impute import SimpleImputer
preprocessor = SimpleImputer(missing_values=numpy.nan, strategy='mean')
X = numpy.array(df1['Benefits']).reshape(-1,1)#targeting special  column named Benefits
preprocessor.fit(X)#fitting preprocessor
X_prep = preprocessor.transform(X)#applying transform function
df1['Mean_Benefits'] = X_prep.reshape(1,-1)[0]#We convert it to the original shape by applying the inverse reshape() function and we store the result into a new column named mean_benefits of the dataframe df1
df1.head()