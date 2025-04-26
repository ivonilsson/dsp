# Tasks
Look at the tasks to make sure everything is done as described.

## Exercise 4: ML with Scikit-Learn

### Linear and polynomial regression
- [x] Linear
- [x] Polynomial regression

### Clustering
- [x] k-Means
- [x] GMM (try setting a random state and n_init=10 etc)

### Decision Trees and Model Validation
#### Decision Tree
- [x] Decision Trees, 80-20 split, use random state
- [x] Test on test-set
- [x] Plot the tree
#### Model Validation
- [x] Plot confusion matrix
- [x] Use Scikit-Learn

### SVMs, Hyperparameters, and Cross-Validation
- [x] Fit a support vector classifier to the data and evaluate its accuracy (Linear kernel, regularization parameter C = 1.0)
- [x] Use same classifier as in task above, perform 10-fold cross-validation, is the result different?
- [x] Perform grid search to find the best kernel and regularization value for the task, atleast test linear and rbf kernel aswell as C=1.0, C=10.0, C=100.0

## Exercise 5: Statistical Modeling and Advanced Topics

### Perumtation with feature importance
- [x] Make prediction then do the step below
- [x] Shuffle values of a given feature column and see how the prediction changes (classification), if its the same, not important, if it gets worse its an important feature
- [x] Calculate feature importance from step above
- [x] Train model again on two most important features
- [x] Train model again on two least important features
- [x] See what accuracy we would get if only guessing majority class

### Statistical testing
- [x] Check if a feature has a normal distribution
- [x] Check which features are correlated
- [x] Do McNemar's tests and compare the classifiers

### Dimensionality reduction
- [x] Perform PCA into 2-dimensional space, 2D is suitable for vizualisation, plot
- [x] Perform t-SNE transformation and plot
- [x] Repeat t-SNE plots with different random states and perplexity values


