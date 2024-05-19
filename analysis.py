# Anderson's/Fisher's Iris Data Set analysis
# author : Nataliia Dragunova

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

# Using a continues numerical variable 'petal_length' for creating a Histogram 'Iris petal length'
fig, ax = plt.subplots()

x = iris_df['petal_length']
plt.hist(x)

ax.set_ylabel('population')
ax.set_title('Iris petal length')

plt.savefig("Iris petal length.png")

# Map species to more readable labels
species_mapping = {'Iris-setosa': 'setosa', 'Iris-versicolor': 'versicolor', 'Iris-virginica': 'virginica'}
iris_df['class'] = iris_df['class'].map(species_mapping)

# Define the feature names
feature_names = column_names[:-1]  # Exclude the species column
species_names = iris_df['class'].unique()

# Plot histograms
plt.figure(figsize=(18, 12))
for i, species in enumerate(species_names):
    for j, feature in enumerate(feature_names):
        plt.subplot(3, 4, i * 4 + j + 1)
        subset = iris_df[iris_df['class'] == species]
        plt.hist(subset[feature], bins=20, color='blue', edgecolor='black')
        plt.title(f'Histogram of {feature}\nfor {species}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

