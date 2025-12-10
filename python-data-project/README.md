# Python Data Analysis Project

## Overview
This repository showcases my data analysis projects using Python and Pandas. It includes data inspection, cleaning, analysis, and visualisation tasks.

## Dataset
The dataset `student.csv` is loaded from Google Drive into Jupyter Notebook, which is used for coding.

```python
from google.colab import drive
drive.mount('/content/drive')
```
Pandas is imported, and a DataFrame is created:

```python
import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/student.csv")
```

## Dataset Description
The dataset contains student information including:
- ID
- Name
- Class
- Mark
- Gender

## Analysis Steps
1. Inspecting the data – understand the dataset, check columns, types, and missing values 🧐  
2. Cleaning missing values – handle missing data and fix errors 🧹  
3. Analysing distributions – explore patterns 📊  
4. Creating visualisations 📈

### 🧐  Inspecting the data
Here you can describe what you did, e.g., used df.info() to check column types and missing values.

### 🧹  Cleaning missing values
Explain how you handled NaN values, corrected inconsistent entries, etc.

### 📊  Analysing distributions
Describe any patterns you explored, e.g., value counts or group averages.

### 📈  Creating visualisations
List the charts you created and what insights they show.






## Results
Short summary of insights or outputs, e.g., charts, top students, trends.

## How to Run
Instructions to open the Jupyter Notebook and reproduce the analysis.

