#Using Python to perform Exploratory Data Analysis on the "IT Salary Survey for EU region(2018-2020) dataset"
#To Import Libraries
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# to load the dataset
df = pd.read_csv('IT Salary Survey for EU region.csv') 

#data cleaning

# Check for null values
df.isnull().sum()

# Drop columns with a high number of missing values
df.drop(['Purchasing Power', 'City'], axis=1, inplace=True)

# Replace missing values with the mean
df.fillna(df.mean(), inplace=True)

# Check for duplicate values
df.duplicated().sum()

#data visualization

# Histogram of Age
sns.histplot(data=df, x='Age')

# Countplot of Gender
sns.countplot(data=df, x='Gender')

# Barplot of Education Level and Salary
sns.barplot(data=df, x='Education Level', y='Salary')

# Scatterplot of Experience and Salary
sns.scatterplot(data=df, x='Experience', y='Salary')

# Heatmap of Correlation Matrix
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

#data analysis

# Histogram of Age
sns.histplot(data=df, x='Age')

# Countplot of Gender
sns.countplot(data=df, x='Gender')

# Barplot of Education Level and Salary
sns.barplot(data=df, x='Education Level', y='Salary')

# Scatterplot of Experience and Salary
sns.scatterplot(data=df, x='Experience', y='Salary')

# Heatmap of Correlation Matrix
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')


