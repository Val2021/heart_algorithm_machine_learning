import pandas as pd
import numpy as np

data = pd.read_csv('heart.csv', sep=',',encoding='iso-8859-1')
#print(data.describe()['Age'].min())

data_01=data.isnull().sum()
#print(data_01)

# Replace missing values ​​with mean
def data_processing_age():
    data_01 = pd.DataFrame(data=data)
    data_01['Age'].fillna(data_01['Age'].mean(), inplace=True)
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






