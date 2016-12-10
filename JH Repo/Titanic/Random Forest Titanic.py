import numpy as np
import pandas as pd
import csv as csv
from sklearn.ensemble import RandomForestClassifier



file_path = '/Users/JohnHanlon/Desktop/Kaggle/Titanic/'


#Data Cleanup
#TRAIN Data

#load the train file into a dataframe
train_df = pd.read_csv('{}train.csv'.format(file_path), header=0)

#Need to convert all strings to integer classifiers
#Need to fill in the missing values of the data and make it complete


#Female = 0, Male = 1
train_df['Gender'] = train_df['Sex'].map({'female':0, 'male':1}).astype(int)



#Embarked from 'C', 'Q', 'S'
#Note this is not ideal: in translating categories to numbers, Part 2 is not 2 
#times greater than Part 1, etc

#All missing Embarked -> just make them embark from the most common place

if len(train_df.Embarked[train_df.Embarked.isnull()]) > 0:
    train_df.Embarked[train_df['Embarked'].isnull()] = train_df.Embarked.dropna().mode().values



#determine all values of Embarked
Ports = list(enumerate(np.unique(train_df['Embarked'])))
Port_dicts = {name : i for i, name in Ports}

train_df.Embarked = train_df.Embarked.map(lambda x: Port_dicts[x]).astype(int)




'''
#Set up a diction in form Ports: Index
Ports_dict = {name : i for i, name in Ports}

#Convert of str Embarked values to int
train_df.Embarked = train_df.Embarked.map(lambda x: Ports_dict[x]).astype(int)

'''


'''
if len(train_df.Embarked[train_df.Embarked.isnull()]) > 0:
	train_df.Embarked[train_df.isnull()] = 
 train_df.Embarked.dropna().mode().values
'''