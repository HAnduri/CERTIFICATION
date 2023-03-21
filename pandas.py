# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 22:01:42 2022

@author: NNalband
"""

import pandas as pd

#-----------Series

a = ['a','b','c']
m= pd.Series(a)
print(type(m))
print(m)
print(m[0])

n = pd.Series(a, index = ["x", "y", "z"])
print(n)
print(n['y'])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

#---------DataFrames

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "type":['a','b','c'],
  "price":[10,20]
}
df= pd.DataFrame(data)
print(df)
print(df.loc[0]) #Locate Row
print(df.loc[[0,1,2]]) #list of indexes of rows

df= pd.DataFrame(data,index=['x','y','z'])
print(df)
print(df.loc['x']) #Locate Row by label only
print(df.loc[['x', 'y'],['type','price']]) #list of indexes of specific rows

print(df.iloc[0]) #locate row by index only
print(df.iloc[0:2]) #lst of rows by row slicing
print(df.iloc[0:2,1:3]) #list of rows and columns by slicing

#---------read and write csv/excel

df.to_csv(r'C:\Users\NNalband\Documents\Session\test1.csv') #write dataFrame into csv

df.to_excel(r'C:\Users\NNalband\Documents\Session\test1.xlsx',sheet_name="diet",index=False)

df1 = pd.read_excel(r'C:\Users\NNalband\Documents\Session\test1.xlsx')
df1
#-----------readCsv
df1 = pd.read_csv(r'C:\Users\NNalband\Documents\Session\sampleData.csv')
print(type(df1.to_string())) 
print(type(df1.head())) #by default takes top 5
print(df1.tail()) #by default takes bottom 5

print(df1['Region'])
print(df1[['Region','Item','Units']])

print(df1.loc[0])
print(df1.iloc[2:4,1])
#-------------Concat

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
print(df, "\n\n", df1)
print(pd.concat([df,df1]))

#-concat by axis
data1 = {'Name':['Jai', 'Princi', 'Goutham', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj']} 
   
data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
        'Age':[22, 32, 12, 52], 
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj']} 
 
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 
print(df, "\n\n", df1)
res2 = pd.concat([df, df1], axis=0)
print(res2)

print(df, "\n\n", df1)
res3= pd.concat([df, df1], axis=1, join='inner')
print(res3)

#-------------merge

data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
   
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
df = pd.DataFrame(data1)  
df1 = pd.DataFrame(data2) 
print(df, "\n\n", df1)
res = pd.merge(df, df1, on='key')
res

#---merge on multiple keys

data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
   
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
   
df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2)
print(df, "\n\n", df1)
#print(df1['Address'])
res1 = pd.merge(df, df1, on=['key', 'key1'])
res1

# using keys from left frame
print(df, "\n\n", df1)
res = pd.merge(df, df1, how='left', on=['key', 'key1'])
res

#--------join

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32]} 
data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
  
df = pd.DataFrame(data1,index=['K0', 'K1', 'K2', 'K3'])
df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])
print(df, "\n\n", df1)
res = df.join(df1)
res

# getting union
res1 = df.join(df1, how='outer')
res1

#--- Querying 

sales_data={"name":["William","Emma","Sofia","Markus","Edward","Thomas","Ethan","Olivia","Arun","Anika","Paulo"],
            "region":["East","North","East","South","West","West","South","West","West","East","South"],
            "sales":[50000,52000,90000,34000,42000,72000,49000,55000,67000,65000,67000],
            "expenses":[42000,43000,50000,44000,38000,39000,42000,60000,39000,44000,45000]}

stores_data={"owner_name":["William","Emma","Sofia","Markus"],
           "no_of_stores":[2,5,3,2]}

sales_data_df = pd.DataFrame(sales_data)
stores_data_df=pd.DataFrame(stores_data)

print(sales_data_df)
print(stores_data_df)

#returns boolean
s1=sales_data_df['sales'] > 50000
print(s1)

#with the boolean, will get the data --where
s2=sales_data_df[sales_data_df['sales'] > 50000]
print(s2)

#Group by 

s3=sales_data_df.groupby(['region']).sum() #all numberic columns group by aggregation

s4=sales_data_df.groupby(['region'])['sales'].sum() #specific column group by aggregation

s5=sales_data_df.groupby(['region'])['region'].count()

print(s3)
print(s4)
print(s5)

#group by specific value from a region

s5=sales_data_df.groupby(['region'])
print(s5.get_group('East'))
print(s5.get_group('East')[['name','sales']])

#Fetch from two tables
#get no_of stores for the names present in both the dataframes

s_df=pd.merge(sales_data_df,stores_data_df,left_on='name',right_on='owner_name')
print(s_df[['owner_name','region','no_of_stores']])

#or 

s2_df=sales_data_df.join(stores_data_df,how='inner')
print(s2_df[['owner_name','region','no_of_stores']])

#or 

s3_df= pd.concat([sales_data_df, stores_data_df], axis=1, join='inner')
print(s3_df[['owner_name','region','no_of_stores']])


#------Manipulate text data

print(sales_data_df['name'].str.lower())
print(sales_data_df['name'].str.len())

#------Plot

print(res)
res.plot(x='Name',y='Age')
res.plot.scatter(x='Name',y='Age')
res.plot.box()

#-----Pandas miscallenaous 
data = {'Name': ['Jai', 'Princi', 'Gaurav',
                 'Anuj', 'Ravi', 'Natasha', 'Riya'],
        'Age': [17, 17, 18, 17, 18, 17, 17],
        'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F'],
        'Marks': [90, 76, 'NaN', 74, 65, 'NaN', 71]}
 
df = pd.DataFrame(data)
print(df)
print(df['Marks'])
df.shape

print(list(df.values))   #list of columns


#----------Missing values
c = avg = 0
for e in df['Marks']:
    if str(e).isnumeric():
        c += 1
        avg += e
avg /= c

# Replace missing values
df1 = df.replace(to_replace="NaN", value=avg)
df1

#-----mean, mode etc., 

df1['Marks'].mean()
df1['Marks'].sum()
df1['Marks'].mode()
df1['Marks'].median()
#---------Reshaping Data

df1['Gender'] = df1['Gender'].map({'M': 0, 'F': 1 }).astype(float)
df1

#---------Filtering Data
print(df1['Marks'] >= 75)
df2 = df1[df1['Marks'] >= 75]
df2

df2 = df2.drop(['Age'], axis=1)
df2

#---------Group By

car_selling_data = {'Brand': ['Maruti', 'Maruti', 'Maruti',
                              'Maruti', 'Hyundai', 'Hyundai',
                              'Toyota', 'Mahindra', 'Mahindra',
                              'Ford', 'Toyota', 'Ford'],
                    'Year':  [2010, 2011, 2009, 2013,
                              2010, 2011, 2011, 2010,
                              2013, 2010, 2010, 2011],
                    'Sold': [6, 7, 9, 8, 3, 5,
                             2, 8, 7, 2, 4, 2]}
 
df4 = pd.DataFrame(car_selling_data)
print(df4)
grouped = df4.groupby('Year')
print(grouped.get_group(2010))

#-----------Duplicate

student_data={'Name': ['Amit', 'Praveen', 'Jagroop',
                         'Rahul', 'Vishal', 'Suraj',
                         'Rishab', 'Satyapal', 'Amit',
                         'Rahul', 'Praveen', 'Amit'],
                'Roll_no': [23, 54, 29, 36, 59, 38,
                            12, 45, 34, 36, 54, 23],
                'Email': ['xxxx@gmail.com', 'xxxxxx@gmail.com',
                          'xxxxxx@gmail.com', 'xx@gmail.com',
                          'xxxx@gmail.com', 'xxxxx@gmail.com',
                          'xxxxx@gmail.com', 'xxxxx@gmail.com',
                          'xxxxx@gmail.com', 'xxxxxx@gmail.com',
                          'xxxxxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com']}

df5 = pd.DataFrame(student_data)
df5
non_duplicate = df5[~df5.duplicated('Roll_no')]
print(non_duplicate)