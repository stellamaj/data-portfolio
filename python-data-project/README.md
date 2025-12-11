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
To understand the dataset, info() was used to review its structure, and the data was displayed as a DataFrame.

```python
df.info()
```
Output:

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 35 entries, 0 to 34
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   id      35 non-null     int64 
 1   name    34 non-null     object
 2   class   34 non-null     object
 3   mark    35 non-null     int64 
 4   gender  33 non-null     object
dtypes: int64(2), object(3)
memory usage: 1.5+ KB
```


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

