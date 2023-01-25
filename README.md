# KNN and PCA model development notebook
## Created by Marvellous Arabambi (University of Bristol)
This repository can be found at : https://github.com/Marv-Arabambi/python_project.git

## Decription
This notebook walks you through the process of using *K-Nearest Neighbors (KNN)* to develop a model which is then fited to a training data set. Using the model, decision boundaries can be decided and prediction made on what class a sample falls. *Principle components analysis (PCA)* is also conducted alongside the KNN inorder to take into consideration relationships between the varaibles when developing the model. 

In the notebook we will use a data set which include different features of tumors. We will develop a model and then make prediction on wheather a tumor is classed as either _benign_ or _malignant_ based on the measurements we later input into the model.  

There is scope within the notebook to use *your own data set* to form a model and then makes some predictions. However, your data set must be formated in a CSV file correctly. It should include columns labled: "mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness", "mean compactness", "mean concavity", "mean concave points", "mean symmetry", "mean fractal dimension". The column representing the $y$ result should only contain values of either 0 (to represent benign diagnoses) or 1 (representing a malignant diagnoses).

## Dependencies
numpy

matplotlib

scikit-learn (1.2.0)

pandas

## Installing
The notebook to downloaded is:

KNN_and_PCA_model_development.ipynb

Files which must also be downloaded, as the script calls on them,  are:

1. plot.py
2. model.py

(remember that these files should be in the same directory as the notebook)

## Execting the Program

Run through the script in the notbook using the markdown cells and annotations as a guide

## Reference
data set was sourced from:
_Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science._
