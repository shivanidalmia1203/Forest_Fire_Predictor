import pandas as pd
import numpy as np
from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score

data = pd.read_csv('forestfires.csv')
adder=pd.read_csv('adder.csv')
dataset=pd.concat([data,adder])


#Getting Independent and Dependent Features
X = dataset.iloc[:, 0:12].values # independent
y = dataset.iloc[:, 12].values # dependent variable
y = dataset.iloc[:, 12].values
for i in range(0, len(y)):
    y[i] = (y[i]*2.47)
    if y[i] < 1.0:
        y[i] = 1
    elif y[i] < 10.0:
        y[i] = 2
    elif y[i] < 100.0:
        y[i] = 3
    elif y[i] < 300.0:
        y[i] = 4
    elif y[i] < 1000.0:
        y[i] = 5
    elif y[i] < 5000.0:
        y[i] = 6
    else:
        y[i] = 7
# Encoding categorical data for independent variables 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 2] = labelencoder_X_1.fit_transform(X[:, 2]) #For month
labelencoder_X_2 = LabelEncoder()
X[:, 3] = labelencoder_X_2.fit_transform(X[:, 3]) #For weekday
onehotencoder = OneHotEncoder(categorical_features = [2])#dummy variable for month
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:] #avoid dummy variable trap 
onehotencoder = OneHotEncoder(categorical_features = [13])#dummy variable for week
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:] #avoid dummy variable trap
'''Encoding For Classification'''
from keras.utils import np_utils
y = np_utils.to_categorical(y)
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train=X[0:516]
X_test=X[517:597]
y_train=y[0:516]
y_test = y[517:597]
# Feature Scaling to optimize 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from keras import backend as K

def recall_m(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

def precision_m(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision

def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    val = 2*((precision*recall)/(precision+recall+K.epsilon()))
    #print(val)
    return val


import keras
from keras.models import Sequential #For Initializing ANN
from keras.layers import Dense #For Layers of ANN
from keras.layers import Dropout
classifier = Sequential()
classifier.add(Dense(units = 17, kernel_initializer = 'uniform', activation = 'relu', input_dim = 27))
classifier.add(Dropout(rate=0.1))
classifier.add(Dense(units = 17, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 17, kernel_initializer = 'uniform', activation = 'relu')) 
classifier.add(Dense(units = 7, kernel_initializer = 'uniform', activation = 'softmax'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


classifier.fit(X_train, y_train, batch_size = 25, epochs = 600)


y_pred = classifier.predict(X_test)

o1=pd.DataFrame(y_pred.max(axis=1))

tester=np.argmax(y_pred,axis=1)

y = np_utils.to_categorical(tester)

output=pd.DataFrame(tester)

un_scale=[1,10,100,300,1000,5000]
def un_scaler(y):
    if y == 1:
        y1='1 acre or less'
    elif y == 2:
        y1 = 'more than one acre, but less than 10 acres'
    elif y == 3:
        y1 = '10 acres or more, but less than 100 acres'
    elif y == 4:
        y1 = '100 acres or more, but less than 300 acres'
    elif y == 5:
        y1 = '300 acres or more, but less than 1,000 acres'
    elif y == 6:
        y1 = '1,000 acres or more, but less than 5,000 acres'
    return y1
    
'''
Classification
#Convert to Acres then Classify Size
Class 1.A - one acre or less;
Class 2.B - more than one acre, but less than 10 acres;
Class 3.C - 10 acres or more, but less than 100 acres;
Class 4.D - 100 acres or more, but less than 300 acres;
Class 5.E - 300 acres or more, but less than 1,000 acres;
Class 6.F - 1,000 acres or more, but less than 5,000 acres;
'''
# # predict probabilities for test set
# yhat_probs = classifier.predict(X_test, verbose=0)
# # predict crisp classes for test set
# yhat_classes = classifier.predict_classes(X_test, verbose=0)

# # reduce to 1d array
# yhat_probs = yhat_probs[:, 0]
# yhat_classes = yhat_classes[:, 0]

# # accuracy: (tp + tn) / (p + n)
# accuracy = accuracy_score(y_test, yhat_classes)
# print('Accuracy: %f' % accuracy)
# # precision tp / (tp + fp)
# precision = precision_score(y_test, yhat_classes)
# print('Precision: %f' % precision)
# # recall: tp / (tp + fn)
# recall = recall_score(y_test, yhat_classes)
# print('Recall: %f' % recall)
# # f1: 2 tp / (2 tp + fp + fn)
# f1 = f1_score(y_test, yhat_classes)
# print('F1 score: %f' % f1)


test=pd.DataFrame(y_test)
test=test.drop([0],axis=1)

test=test.drop([6],axis=1)

o2=output[0].apply(un_scaler)
o2=pd.DataFrame(o2)

o1.columns=["percentage"]
o2.columns=["desc"]

outing=pd.concat([o1,o2],axis=1)

outing.iloc[0]

outing.to_json('percent.json')


classifier.save("ANN.h5")



