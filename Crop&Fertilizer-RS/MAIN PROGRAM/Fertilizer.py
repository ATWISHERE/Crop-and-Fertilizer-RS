# import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import warnings
warnings.filterwarnings('ignore')


# load the dataset
fertilizer = pd.read_csv("Dataset/Fertilizer Prediction.csv")

# Only select the numerical columns 
features = fertilizer.select_dtypes(include=[np.number]).columns.tolist()
print(f"WE CAN TARGET OUR FERTILIZER FROM GIVEN FEATURES\n{features}\n--------Please provide data Accordingly--------\n  ")

#### Encoding the target column
fert_dict = {
'Urea':1,
'DAP':2,
'14-35-14':3,
'28-28':4,
'17-17-17':5,
'20-20':6,
'10-26-26':7,
}
fertilizer['fert_no'] = fertilizer['Fertilizer Name'].map(fert_dict)
y=fertilizer['fert_no']


# drop the target column with name and keep the target column with numbers
fertilizer.drop('Fertilizer Name',axis=1,inplace=True)



# convert the categorical columns to numerical columns using labelencoder
lb = LabelEncoder()
fertilizer["Soil Type"]=lb.fit_transform(fertilizer['Soil Type'])
fertilizer['Crop Type']=lb.fit_transform(fertilizer['Crop Type'])


X=fertilizer.drop('fert_no',axis=1)

# split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)


### Scaling
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
print(f"You can trust our System as we have Measured\nAccuracy score upto {acs*100:.2f}% so Please")

#Prediction
def fert_rec(temp,hum,Mois,Stype,Ctype,N,K,P):
    features=np.array([[temp,hum,Mois,Stype,Ctype,N,K,P]])
    transformed_features=scaler.transform(features)
    prediction=dtc.predict(transformed_features).reshape(1,-1)
    fert_dict = {1: 'Urea', 2: 'DAP', 3: '14-35-14', 4: '28-28', 5: '17-17-17', 6: '20-20', 7: '10-26-26'}
    fertilizer=[fert_dict[i]for i in prediction[0]]
    return f"{fertilizer} is the best fertilizer for the given conditions.\n--------THANKYOU--------\n  " 




# Given input values

temp=float(input("Enter Temperature T(°C): "))
hum=float(input("Enter Humidity H (%): "))
Mois = float(input("Enter Moisture M: "))
Stype = float(input("Enter Soil Type \n1.Sandy\n2.Loamy\n3.Black\n4.Red\n5.Clayey\nST: "))
Ctype = float(input("Enter Crop Type\n1.Maize\n2.Sugarcane\n3.Cotton\n4.Tobacco\n5.Paddy\n6.Barley\n7.Wheat\n8.MilletsOil seeds\n9.Pulses\n10.Ground Nuts' CT: "))
N = float(input("Enter Nitrogen N: "))
K = float(input("Enter Potassium K: "))
P = float(input("Enter Phosphorous P: "))
a=fert_rec(temp,hum,Mois,Stype,Ctype,N,K,P)
print(a)                                                