import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

# loading the digits data
digits = datasets.load_digits()
X = digits.data    # the data, 1797 x 64 array
y = digits.target # target information
digitsFeatureNames = digits.target_names  # digits
digitsString = [str(i) for i in digitsFeatureNames]



# using a grid search
param = {'n_neighbors':list(range(5,100,10)),
         'weights':['uniform', 'distance']}
kNN = KNeighborsClassifier()
grid_kNN = GridSearchCV(kNN, param, cv=5)
grid_kNN.fit(X,y)
print(grid_kNN.best_params_)
print(grid_kNN.best_score_)



# Checking the winning combination
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
                                                    random_state=333)
kNN = KNeighborsClassifier(5, weights='distance')
kNN.fit(X_train,y_train)
y_pred = kNN.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test, y_pred,
                            target_names=digitsString))
