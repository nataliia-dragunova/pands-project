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


# Set the aesthetics for the plots in seaborn
sns.set(style="whitegrid")

# Get the unique classes (species)
classes = iris_df['class'].unique()

# Iterate through each class and each numeric column
for cls in classes:
    class_df = iris_df[iris_df['class'] == cls]  # Filter the dataframe for the current class
    for column in iris_df.columns[:-1]:  # Exclude the 'class' column for individual histograms
        plt.figure(figsize=(10, 6))  # Set the size of the figure
        sns.histplot(class_df[column], bins=20, kde=False, color='blue')
        plt.title(f'Histogram of {column} for {cls}')
        plt.xlabel(column)
        plt.ylabel('Population')
        # Save each histogram as a .png file, including the class name in the filename
        plt.savefig(f'{cls}_{column}_histogram.png')

# Define the pairs of variables to plot
variable_pairs = [('petal_length', 'petal_width'), ('sepal_length', 'sepal_width')]

# Get the unique classes (species)
classes = iris_df['class'].unique()

# Loop through each class and each pair of variables
for cls in classes:
    class_df = iris_df[iris_df['class'] == cls]  # Filter the dataframe for the current class
    for (x_col, y_col) in variable_pairs:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=class_df, x=x_col, y=y_col, hue='class', palette='Set1', s=100, edgecolor='black')
        plt.title(f'Scatter Plot of {x_col} vs {y_col} for {cls}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.legend(title='Class')
        # Save each scatter plot as a .png file, including the class name and variable names in the filename
        plt.savefig(f'{cls}_{x_col}_vs_{y_col}_scatter.png')