# Data Mining #

In this repository, there is Python code that reads a dataset showing company profits based on their investments in different areas. With this dataset, we perform the following tasks:

1. **Categorical variable encoding**: Convert categorical variables into numerical formats using encoding techniques like one-hot encoding or label encoding, which is essential for model training.

2. **Data exploration and outlier analysis**: Perform exploratory data analysis (EDA) to understand the distribution and relationships within the data. We also identify and handle outliers that could distort the results of the model.

3. **Data standardization**: Standardize the dataset to ensure that all features contribute equally to the model. This involves scaling the data so that it has a mean of zero and a standard deviation of one.

4. **Decision trees for profit estimation**: Use decision tree models to estimate the `profit` variable. Decision trees are intuitive models that split the data based on feature values to predict the target variable.

5. **Hyperparameter optimization using Grid Search CV**: Optimize the hyperparameters of the decision tree model by performing Grid Search with cross-validation. This helps in finding the best model configuration for improved performance.

6. **Train-test split**: Split the dataset into training and testing sets to evaluate the model's performance. The training set is used to train the model, while the test set is used to assess its accuracy.

7. **Error calculation**: Calculate the errors made by the model on the test set, such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or other relevant metrics, to evaluate model performance.

---

Additionally, we read a Pokémon dataset where we attempt to predict the Pokémon class based on its attributes. For this task, we use several classification algorithms:

1. **Decision Trees for classification**: Apply decision trees to classify Pokémon into different categories based on their attributes, leveraging the model's ability to handle both numerical and categorical data.

2. **Naive Bayes**: Use the Naive Bayes classifier, which is based on Bayes' theorem, to predict the Pokémon class. This probabilistic model is particularly effective for datasets with categorical features.

3. **K-Nearest Neighbors (KNN)**: Implement the KNN algorithm, which classifies a Pokémon based on th