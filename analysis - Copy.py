# Anderson's/Fisher's Iris Data Set analysis
# author : Nataliia Dragunova + ChatGPT

# Load libraries that perspectively will be used in analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the column names as in "Attribute Information" in iris.name file
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Load the dataset as .csv file with column names defined
iris_df = pd.read_csv('iris.data', header=None, names=column_names)

# Check the first few rows
print(iris_df.head())

# Outputs a summary of each variable to a single text file
# Method to_csv where index=False for excluding row numbers in text
for column in iris_df.columns:
    filename = f"{column}.txt"
    iris_df[column].to_csv(filename, index=False, header=True)


