import sklearn as skl
import numpy
from sklearn.datasets import load_iris
iris_dataset=load_iris ()
print ("Type of Target:{}".format(type(iris_dataset['target'])))