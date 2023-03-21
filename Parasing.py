# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:57:01 2022

@author: NNalband
"""

import pandas as pd
import json
import xmltodict

#--------JSON

#1 json data 
f=open(r'C:\Users\NNalband\Documents\Session\New folder\json_sample_1.json')
json_dict=json.load(f)
print(type(json_dict[0]))

for i in json_dict:
    if i['gender']=='Female':
        i['gender']='F'
    elif i['gender']=='Male':
        i['gender']='M'
print(json_dict)
#conversion into json again
out_json=json.dumps(json_dict)
print(out_json)

#2
f=open(r'C:\Users\NNalband\Documents\Session\New folder\json_sample_2.json')
json_dict=json.load(f)
print(json_dict)

print(json_dict['className']['associatedDrug#2'][0]['strength'])

for drug in json_dict['className']:
    print(drug)
    print(json_dict['className'][drug][0]['name'])
    if json_dict['className'][drug][0]['strength']=='500 mg':
        json_dict['className'][drug][0]['dose']='Core'
    else:
        json_dict['className'][drug][0]['dose']='Mild'
print(json_dict)
x=json.dumps(json_dict)
print(x)

#3
f=open(r'C:\Users\NNalband\Documents\Session\New folder\json_sample_3.json')
json_dict=json.load(f)
print(json_dict)

print(json_dict['glossary']['title'])
print(['glossary']['GlossDiv']['GlossList']['GlossEntry']['Abbrev'])

s=json_dict['glossary']['GlossDiv']['GlossList']['GlossEntry']
print(s['GlossDef']['GlossSeeAlso'][1])

#4 json data in a text file 
f=open(r'C:\Users\NNalband\Documents\Session\New folder\json_sample_4.txt')
json_dict=json.load(f)
print(json_dict)

for i in json_dict:
    print(i['userId'])

#-------------XML

#1 xml data in text file 
f=open(r'C:\Users\NNalband\Documents\Session\New folder\xml_sample_1.txt').read()
ord_dict=xmltodict.parse(f)
print(json.dumps(ord_dict))
xml_dict=json.loads(json.dumps(ord_dict))

print(xml_dict)

for st in xml_dict['data']['student']:
    print(st)
    print(st['email'])
    if st['grade']=='A':
        st['grade']='A+'
print(xml_dict)
#conversion into xml again
out_xml=xmltodict.unparse(xml_dict)
print(out_xml)

#2
f=open(r'C:\Users\NNalband\Documents\Session\New folder\xml_sample_2.xml').read()
ord_dict=xmltodict.parse(f)
print(json.dumps(ord_dict))
xml_dict=json.loads(json.dumps(ord_dict))
print(xml_dict)


for ct in xml_dict['data']['customer']:
    if ct['phone']:
        print('Avl')
    else:
        print('Unavl')

for customer in xml_dict['data']['customer']:
    print(customer)
    try:
        if (customer['phone']):
            customer['calling']='available'
    except KeyError:
        customer['calling']='unavailable'
        
print(xml_dict)
#conversion into xml again
out_xml=xmltodict.unparse(xml_dict)
print(out_xml)




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