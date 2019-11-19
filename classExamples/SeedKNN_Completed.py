import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# loadin the data
seedData = pd.read_csv('seeds_dataset.txt', sep='\t', header=None)
X = np.array(seedData.iloc[:,:7])   # features (7 variables)
y = np.array(seedData.iloc[:,7])    # target labels
targetNames = ['Kama','Rosa','Canadian']


# spliting the data into training and testing data sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=70,
                                                    random_state=1234)


# EXERCISE: Define classifier object, train it, and predict
# k nearest neighbor classifier objects
kNN = KNeighborsClassifier(10, weights='uniform')
kNN.fit(X_train,y_train)
y_pred = kNN.predict(X_test)

# EXERCISE: Generate confusion matrix, classification report
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test, y_pred,
                            target_names=targetNames))


# kNN classifier, k=20 and weights=distance
kNN = KNeighborsClassifier(20, weights='distance')
kNN.fit(X_train,y_train)
y_pred = kNN.predict(X_test)
# classifier performance
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test, y_pred,
                            target_names=target_names))
