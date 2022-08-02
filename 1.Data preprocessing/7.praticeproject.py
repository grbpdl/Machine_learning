'''
DESCRIPTION

From the raw data below, create a data frame:

'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 'last_name': ['Miller', 'Jacobson', ".", 'Milner','Cooze'],

'age': [42, 52, 36, 24, 73], 'preTestScore': [4, 24, 31, ".", "."],'postTestScore': ["25,000", "94,000", 57, 62, 70]

Objective: Perform data processing on the raw data.

Actions to perform:

Save the data frame into a .csv file as project.csv
Read the project.csv file and print the data frame.
Read the project.csv file without column heading.
Read the project.csv file and make two index columns, namely, 'First Name' and 'Last Name'.
Print the data frame in a Boolean form as True or False. True for Null/ NaN values and false for non-null values.
Read the data frame by skipping the first 3 rows and print the data frame.
This is a non-gradable project.
'''
import numpy as np
import pandas as pd
given_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Coze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
#creating dataframe from raw data
# Read the project.csv file and print the data frame.
# df = pd.DataFrame(given_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
# df.to_csv ("E:\learn\machine learning\project.csv")
# print(df)

#Read the project.csv file without column heading.
# df = pd.read_csv('project.csv', header=None)
# print(df)
# Read the project.csv file and make two index columns, namely, 'First Name' and 'Last Name'.
# df = pd.read_csv('project.csv', index_col=['First Name', 'Last Name'], names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
# print(df)

#Print the data frame in a Boolean form as True or False. True for Null/ NaN values and false for non-null values.
# df = pd.read_csv('project.csv', na_values=['.'])
# print(pd.isnull(df))
# Read the data frame by skipping the first 3 rows and print the data frame.
df = pd.read_csv('project.csv', skiprows=3)
print(df)