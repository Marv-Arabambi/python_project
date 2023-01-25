# Creates a function called optimise model which takes 4 argument: train_X_s, train_y_s, test_X_s, test_y_s. The training and testing data sets
def optimise_model(train_X_s, train_y_s, test_X_s, test_y_s): 
    import numpy as np                                                    # for working with arrays and DataFrames
    import pandas as pd                                                   # for storing our DataFrames
    from sklearn.decomposition import PCA                                 # to conduct the PCA
    from sklearn.neighbors import KNeighborsClassifier                    # we would be using a K Neightbours model
    from sklearn.preprocessing import StandardScaler                      # for rescaling each variable
    from sklearn.pipeline import make_pipeline                            # to make a pipeline we can pass our data through
    from sklearn.model_selection import GridSearchCV                      # for optimising the hyper-parameters

    results = pd.DataFrame([])  # an empty DataFrame we can fill as we go through the loop below
    
    for i in range(1,51):      # for loop which will run the GridSearch with different number of PCA components and neighbour
        model = GridSearchCV(
            make_pipeline(
                StandardScaler(),   #rescale inorder to take into account the different scales of the different x values, helps to plot the model better
                PCA(),
                KNeighborsClassifier(n_neighbors=i) # loop through differing number of neighbour
            ),
            {
                "pca__n_components" : range(1, 10), # GridSearch will loop through and give the optimum PCA 
            }                                       # for the current value of i (number of neighbour)
        )
        model.fit(train_X_s, train_y_s)        # fit best model, with current i value, to training data
        score = model.score(test_X_s, test_y_s)      #use test data to score the model
        best_pca = model.best_estimator_["pca"].n_components_   #give value of the optimum PCA component value for 
                                                                #the current number of neighbour tested
        results = results.append(pd.DataFrame({"number of neighbours": i, "best PCA": best_pca, "score": score}, 
                                              index= [0]), ignore_index=True)    # put all the results in a table 

    return(results)   # function returns this table
   
