from sklearn.datasets import load_iris
import scipy as sc
import matplotlib.pyplot as mt
import pandas as pd
import numpy as np
import mglearn 
import matplotlib

iris_dataset= load_iris()
#Checking Data type, features of data, target names and description of data set
print ("keys of iris_dataset: \n{}".format(iris_dataset.keys()))
print (iris_dataset["DESCR"] [:193]+"\n retriveal end")
print ("Target Names: {}".format(iris_dataset['target_names']))
print ("Target Names: {}".format(iris_dataset['feature_names']))
print ("Type of Data: {}".format (type(iris_dataset['data'])))
print ("Shape of Data:{}".format(iris_dataset["data"].shape))
print ("First Five Columns of Data:\n{}".format(iris_dataset['data'][:5]))
print ("Type of Target:{}".format(type(iris_dataset['target'])))
print ("Shape of target: {}".format(iris_dataset["target"].shape))
print ("Shape of target: {}".format(iris_dataset["target"]))

#Split Training and Test Data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(iris_dataset['data'], iris_dataset["target"], random_state=0)
print ("X_train shape:{}".format(x_train.shape))
print ("Y_train shape:{}".format(y_train.shape))

print ("X_test shape:{}".format(x_test.shape))
print ("Y_test shape:{}".format(y_test.shape))

# create dataframe from data in X_train
# label the columns using the strings in iris_dataset.feature_names
iris_dataframe= pd.DataFrame(x_train, columns= iris_dataset.feature_names)
Scatter=pd.plotting.scatter_matrix (iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
 hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)

#Building Model 
#Using the K-Nearest Neigbors 
from sklearn.neighbors import  KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)
print (knn.fit(x_train, y_train))

#Model prediction setup
x_predict= np.array ([[15,10.9,12,0.15]])
print ("x_predict.shape:{}" .format(x_predict.shape))

prediction= knn.predict(x_predict)
print ("Prediction:{}".format(prediction))
print ("prediction:{}" .format(iris_dataset['target_names'] [prediction]))

#Model Evaluation Process
y_pred= knn.predict(x_test)
print ("test set predictions:\n{}".format (y_pred))
print ("Test set score: {:.2f}".format (np.mean(y_pred==y_test)))
Test_Score =  ( "{:.2f}".format((float(knn.score(x_test,y_test)))/1 *100))
print ("Test_Store:",Test_Score, "%")

if float (Test_Score)<  float (50):
    print ("Poor_Model_Prediction")
elif float ( Test_Score) <= float (70):
    print ("Fair Model Prediction")
else :
    print ("Good_Model_Prediction")