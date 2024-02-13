import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mglearn as mg
import sklearn as skl

   # generate dataset

X, y = mg.datasets.make_forge()
# plot dataset
mg.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First feature")
plt.ylabel("Second feature")
#print (("X.shape: {}".format(X.shape)))


x,y =mg.datasets.make_wave (n_sample=40)
plt.plot(x,y,'o')
plt.ylim(-3,3)
plt.xlabel ("Feature")
plt.ylabel ("Target")


from sklearn.datasets import load_breast_cancer
cancer=load_breast_cancer ()
print ("cancer keys():\n {}".format(cancer.keys ()))

print ("shape of cancer data:{}". format(cancer.data.shape))
print ("sample counts per class:\n{}".format(
   {n: v for n , v in zip  (cancer.target_names, np.bincount(cancer.target) )}))
print ("feature names: \n{}". format (cancer.features.name))

from sklearn.datasets import load_boston
boston=load_boston()
print ("data shape for boston:{}".format(boston.data.shape))
x,y=mg.datasets.load_extended_boston()
print ( "X.shape:{}"  .format(x_shape))
mg.plots.plots_knn_classification (n_neigbors=3)

from sklearn.model_selection import train_test_split
x,y=mg.datasers.make_forge()
x_train,x_test,y_train, y_test= train_test_split (x,y, random_state= 0)
from sklearn.neighbors import KNeighborsClassifier
classifier= KNeighborsClassifier(n_neighbors=3)
classifier.fit (x_train, y_train)
print ("test prediction: {}" .format (classifier.predict(x_test)))
print ("test set acuuracy: {2f}". format ((classifier.predict(y_test, x_test))))

#plane coloration 
fig, axis = plt.subplots (1,3, figsize= 10)
for n_neigbors, ax in zip [1,3,9], axis:
   clf=KNeighborsClassifier(n_neigbors=n_neigbors). fit(x,y)
mg.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
mg.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
ax.set_title("{} neighbor(s)".format(n_neighbors))
ax.set_xlabel("feature 0")
ax.set_ylabel("feature 1")
axis[0].legend(loc=3)
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
 cancer.data, cancer.target, stratify=cancer.target, random_state=66)
training_accuracy = []
test_accuracy = []
# try n_neighbors from 1 to 10
neighbors_settings = range(1, 11)
for n_neighbors in neighbors_settings:
 # build the model
 clf = KNeighborsClassifier(n_neighbors=n_neighbors)
 clf.fit(X_train, y_train)
 # record training set accuracy
 training_accuracy.append(clf.score(X_train, y_train))
 # record generalization accuracy
 test_accuracy.append(clf.score(X_test, y_test))
plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
mg.plots.plot_knn_regression(n_neighbors=3)

from sklearn.neighbors import KNeighborsRegressor
X, y = mglearn.datasets.make_wave(n_samples=40)
# split the wave dataset into a training and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# instantiate the model and set the number of neighbors to consider to 3
reg = KNeighborsRegressor(n_neighbors=3)
# fit the model using the training data and training targets
reg.fit(X_train, y_train)
print("Test set predictions:\n{}".format(reg.predict(X_test)))
