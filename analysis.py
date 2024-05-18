# Anderson's/Fisher's Iris Data Set analysis
# author : Nataliia Dragunova



import pandas as pd

# Define the column names
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Load the dataset into a pandas DataFrame
iris_df = pd.read_csv('iris.data', header=None, names=column_names)

# Display the first few rows of the DataFrame
print(iris_df.head())
