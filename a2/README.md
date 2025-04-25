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
- [ ] Decision Trees, 80-20 split, use random state
- [ ] Test on test-set
#### Model Validation
- [ ] Plot confusion matrix
- [ ] Use Scikit-Learn

### SVMs, Hyperparameters, and Cross-Validation
- [ ] Fit a support vector classifier to the data and evaluate its accuracy (Linear kernel, regularization parameter C = 1.0)
- [ ] Use same classifier as in task above, perform 10-fold cross-validation, is the result different?
- [ ] Perform grid search to find the best kernel and regularization value for the task, atleast test linear and rbf kernel aswell as C=1.0, C=10.0, C=100.0

## Exercise 5: Statistical Modeling and Advanced Topics

### Perumtation with feature importance
- [ ] Make prediction then do the step below
- [ ] Shuffle values of a given feature column and see how the prediction changes (classification), if its the same, not important, if it gets worse its an important feature
- [ ] Calculate feature importance from step above
- [ ] Train model again on two most important features
- [ ] Train model again on two least important features
- [ ] See what accuracy we would get if only guessing majority class

### Statistical testing
- [ ] Check if a feature has a normal distribution
- [ ] Check which features are correlated
- [ ] Read on task 8 and do it, too long to write here
- [ ] Do McNemar's tests and compare the classifiers

### Dimensionality reduction
- [ ] Perform PCA into 2-dimensional space, 2D is suitable for vizualisation, plot
- [ ] Perform t-SNE transformation and plot
- [ ] Repeat t-SNE plots with different random states and perplexity values


