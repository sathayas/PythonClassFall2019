import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


# loading the digits data
digits = datasets.load_digits()
X = digits.data    # the data, 1797 x 64 array
digitsImages = digits.images  # image data, 1797 x 8 x 8
y = digits.target # target information
digitsFeatureNames = digits.target_names  # digits


# examples of the digits data
plt.figure(figsize=(8,3))
for iImg in range(3):
    for jImg in range(10):
        plt.subplot(3,10,iImg*10+jImg+1)
        plt.imshow(digitsImages[iImg*10+jImg], cmap=plt.cm.gray_r,
                   interpolation='nearest')
        plt.xticks(())
        plt.yticks(())
plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.show()


# spliting the data into training and testing data sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=.25,
                                                    random_state=0)


# Classifier
