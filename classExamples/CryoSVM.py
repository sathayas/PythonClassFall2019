import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


# loading the data
CryoData = pd.read_csv('Cryotherapy.csv')


# plotting the scatter plot matrix
pd.plotting.scatter_matrix(CryoData.loc[:,['Age','Time','Area']],
                           figsize=[7,7], c=CryoData.Success)
plt.show()


# extracting the features and labels
X = np.array(CryoData.loc[:,['Age','Time','Area']])
y = np.array(CryoData.Success)
targetNames = ['Failure', 'Success']

# Creating the training and testing data sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=30,
                                                    random_state=0)

# Training the SVM classifier
sv = SVC(kernel='linear', C=1.0)
sv.fit(X_train,y_train)

# predicted outcome
y_pred = sv.predict(X_test)

# Confusion matrix
print(confusion_matrix(y_test,y_pred))

# classification report
print(classification_report(y_test, y_pred))
