import pandas as pd
import numpy as np

data = pd.read_csv('heart.csv', sep=',',encoding='iso-8859-1')
#print(data.describe()['Age'].min())

data_01=data.isnull().sum()
#print(data_01)

# Replace missing values ​​with mean
def data_processing_age():
    data_01 = pd.DataFrame(data=data)
    data_01['Age'] = data['Age'].fillna(data_01['Age'].mean()).astype(int)
    return data_01


#print(data_processing_age()['Age'].mean())
# Deleting missing record with pressure equal to zero
def del_pressure_zero():
    delzero = data_processing_age()
    delzero_01=delzero.loc[delzero.RestingBP != 0]
    return delzero_01

#print(del_pressure_zero().Cholesterol.value_counts())

# As the distribution tends to be a normal distribution, let's substitute Cholesterol = 0 for the mean

def cholesterol_mean():
    choleszero = del_pressure_zero()
    choleszero.Cholesterol.replace(0,np.NaN, inplace= True)
    choleszero['Cholesterol'].fillna(choleszero['Cholesterol'].mean(), inplace=True)
    return choleszero

# Transforming nominal categorical variables into ordinal categorical variables

def ord_variables():
    ord=cholesterol_mean()
    ord_replaced = pd.DataFrame.copy(ord)
    ord_replaced['Sex'].replace({'M':0,'F':1},inplace=True)
    ord_replaced['ChestPainType'].replace({'TA':0,'ATA':1,'NAP':2,'ASY':3},inplace=True)
    ord_replaced['RestingECG'].replace({'Normal':0,'ST':1,'LVH':2},inplace=True)
    ord_replaced['ExerciseAngina'].replace({'N':0,'Y':1},inplace=True)
    ord_replaced['ST_Slope'].replace({'Up':0,'Flat':1,'Down':2},inplace=True)
    return ord_replaced


#separating the predictor attributes

def predictors_attr():
    predictors = ord_variables().iloc[:,0:11].values
    return predictors


# Separating target column HeartDisease

def target_attr():
    target = ord_variables().iloc[:,11].values
    return target

print(target_attr().shape)








