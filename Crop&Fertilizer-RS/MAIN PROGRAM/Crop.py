## Crop and Fertilizer Recommendation System Using ML
# pip install numpy,pandas,matplotlib.pyplot,seaborn,scikitlearn

# surpassing warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn.utils.validation")


# Importing Necessary Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Loading The Dataset

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path dynamically
file_path = os.path.join(current_dir, "Dataset", "Crop_recommendation.csv")

# Load the dataset
crop = pd.read_csv(file_path)


#Removed label features list
features=crop.columns.to_list()
features.remove('label')
print(f"WE CAN TARGET OUR CROP FROM GIVEN FEATURES\n{features}\n--------Please provide data Accordingly--------\n  ")

#2. Create a correspondig Dictionary for our labels
crop_dict={
'rice':1,
'maize':2,
'chickpea':3, 
'kidneybeans':4,
'pigeonpeas':5,
'mothbeans':6,
'mungbean':7,
'blackgram':8 , 
'lentil':9,
'pomegranate':10,
'banana':11,
'mango':12, 
'grapes':13, 
'watermelon':14, 
'muskmelon':15, 
'apple':16,
'orange':17,
'papaya':18,
'coconut':19,
'cotton':20,
'jute':21,
'coffee':22
}

   
#3. Assigning dict to new column
crop['crop_no']=crop['label'].map(crop_dict)
y=crop['crop_no']



#4. Dropping label column so that no string should interrupt our data
crop.drop('label',axis=1,inplace =True)
X = crop.drop('crop_no', axis=1)




from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#scaling
from sklearn.preprocessing import StandardScaler
scaler =StandardScaler()
X_train_scaled =scaler.fit_transform(X_train)
X_test_scaled =scaler.transform(X_test)

#Training the Model
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
dtc =DecisionTreeClassifier()
dtc.fit(X_train_scaled,y_train)
# LETS TEST IT
y_pred =dtc.predict(X_test_scaled)
acs=accuracy_score(y_test,y_pred) 
print(f'You can trust our System as we have Measured\nAccuracy score upto {acs*100:.2f}% so Please')

#Prediction
def crop_rec(N,P,K,temp,hum,ph,rain):
    features=np.array([[N,P,K,temp,hum,ph,rain]])
    transformed_features=scaler.transform(features)
    prediction=dtc.predict(transformed_features).reshape(1,-1)
    crop_dict={
               1:'rice',
               2:'maize',
               3:'chickpea', 
               4:'kidneybeans',
               5:'pigeonpeas',
               6:'mothbeans',
               7:'mungbean',
               8:'blackgram' , 
               9:'lentil',
               10:'pomegranate',
               11:'banana',
               12:'mango', 
                13:'grapes', 
               14:'watermelon', 
               15:'muskmelon', 
               16:'apple',
               17:'orange',
               18:'papaya',
               19:'coconut',
               20:'cotton',
               21:'jute',
               22:'coffee'}
    crop=[crop_dict[i]for i in prediction[0]]
    return f'{crop} is the best Crop to grow for this condition.\n--------THANKYOU--------\n  '

# #predicting with values
# N=float(input("Enter Nitrogen N: "))
# P=float(input("Enter Phosphorous P: "))
# K=float(input("Enter Potassium K: "))
# temp=float(input("Enter Temperature T(°C): "))
# hum=float(input("Enter Humidity H (%): "))
# ph=float(input("Enter pH Value of Soil ph: "))
# rain=float(input("Enter rainfall (mm): "))

# a=crop_rec(N,P,K,temp,hum,ph,rain)
# print(a)
