# KNN and PCA model development notebook
## Created by Marvellous Arabambi (University of Bristol)
This repository can be found at : https://github.com/Marv-Arabambi/python_project.git

## Decription
This notebook walks you through the process of using *K-Nearest Neighbors (KNN)* to develop a model which if fited to a training data set. Using the model, decision boundaries can be decided and prediction made on what class a sample falls. *Principle components analysis (PCA)* is conducted alongside the KNN inorder to take into consideration relationships between varaibles when developing the model. 

Here we are working though a data set which include different features of tumors. We will develop a model and then make prediction on wheather our tumor is classed as either _benign_ or _malignant_ based on the measurements we input to the model. 

There is scope with in the notebook to use *your own data set* to form a model and then makes some predictions. Your data set must be formated in a CSV file correctly. However, your columns should include thoese labled: "mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness", "mean compactness", "mean concavity", "mean concave points", "mean symmetry", "mean fractal dimension". The column representing the $y$ result should only contain values of either 0 (to represent benign diagnoses) or 1 (representing a malignant diagnoses)

## Dependencies
numpy

matplotlib

scikit-learn (1.2.0)

## Installing
The notebook to be downloaded is:

KNN_and_PCA_model_development.ipynb

The file that also must be downloaded that the script calls are:

1. plot.py
2. model.py

(remember that these files should be in the same directory as the notebook)

## Execting the Program

Run through the script in the notbook using the markdown cells and annotations as guide

## Reference
data set was sourced from:
_Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science_

