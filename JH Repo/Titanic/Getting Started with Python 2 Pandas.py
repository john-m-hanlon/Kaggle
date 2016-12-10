import csv as csv
import numpy as np 
import pandas as pd 

csv_file_object = csv.reader(open('train.csv', 'rU'))
header = next(csv_file_object)
data = []

for row in csv_file_object:
    data.append(row)

data = np.array(data)

print(data.shape)
print(data[0:15,5])

print(np.ndarray)

df = pd.read_csv('train.csv', header=0)
print(type(df))

print(df.dtypes)

print(df.info())

print(df.describe())

print(df['Age'][0:10])

print(df.Age[0:10])

print(df.Cabin[0:10])

print(type(df['Age']))

print(df['Age'].mean())

print(df['Age'].median())

print(df[['Sex', 'Pclass', 'Age']])

print(df[df['Age'] > 60])

print(df[df['Age'] > 60][['Sex', 'Pclass', 'Age', 'Survived']])
print(df[df['Age'].isnull()][['Sex', 'Pclass' ,'Age']])

for i in range(1,4):
	print(i, len(df[(df['Sex'] == 'male') & (df['Pclass'] == i)]))

import pylab as P 

df['Age'].dropna().hist(bins=16, range=(0,80), alpha=.5)
#P.show()

df['Gender'] = 4
df['Gender'] = df['Sex'].map(lambda x: x[0].upper())

df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1}).astype(int)

median_ages = np.zeros((2,3))
print(median_ages)


for i in range(0, 2):
	for j in range(0, 3):
		median_ages[i, j] = df[(df['Gender'] == i) & (df['Pclass'] == j+1)]['Age'].dropna().median()

print(median_ages)

df['AgeFill'] = df['Age']
df.head()

print(df[df['Age'].isnull()][['Gender', 'Pclass', 'Age', 'AgeFill']].head(10))

for i in range(0, 2):
	for j in range(0, 3):
		df.loc[(df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1), 'AgeFill'] = median_ages[i, j]

print(df[df['Age'].isnull()][['Gender', 'Pclass', 'Age', 'AgeFill']].head(10))

df['AgeIsNull'] = pd.isnull(df.Age).astype(int)

df['Family Size'] = df['SibSp'] + df['Parch']
df['Age*Class'] = df.AgeFill * df.Pclass


df['Age*Class'].dropna().hist(bins=16, range=(0,80), alpha=.5)
#P.show()

print(df.dtypes)


