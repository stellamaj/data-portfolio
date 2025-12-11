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
>From the `info()` output, there are 35 total entries. However, the columns `name` and `class` each show 34 non-null values, which means they contain 1 missing value each. The `gender` column has 33 non-null values, so it contains 2 missing values.

To view the rows with `NaN` values, the DataFrame can be displayed using `df` in Jupyter Notebook for a rich view, or printed with `print(df)`:

Output from print(df):

```
    id         name  class  mark  gender
0    1     John Deo   Four    75  female
1    2     Max Ruin  Three    85    male
2    3       Arnold  Three    55    male
3    4   Krish Star   Four    60  female
4    5    John Mike   Four    60  female
5    6    Alex John   Four    55    male
6    7  My John Rob  Fifth    78    male
7    8       Asruid   Five    85    male
8    9      Tes Qry    Six    78     NaN
9   10     Big John   Four    55  female
10  11       Ronald    Six    89  female
11  12        Recky    Six    94  female
12  13          Kty  Seven    88  female
13  14         Bigy  Seven    88  female
14  15     Tade Row    NaN    88    male
15  16        Gimmy   Four    88    male
16  17        Tumyu    Six    54    male
17  18        Honny   Five    75    male
18  19        Tinny   Nine    18    male
19  20       Jackly   Nine    65  female
20  21   Babby John   Four    69  female
21  22       Reggid  Seven    55  female
22  23        Herod  Eight    79    male
23  24    Tiddy Now  Seven    78    male
24  25     Giff Tow  Seven    88    male
25  26       Crelea  Seven    79    male
26  27          NaN  Three    81     NaN
27  28    Rojj Base  Seven    86  female
28  29  Tess Played  Seven    55    male
29  30    Reppy Red    Six    79  female
30  31  Marry Toeey   Four    88    male
31  32    Binn Rott  Seven    90  female
32  33    Kenn Rein    Six    96  female
33  34     Gain Toe  Seven    69    male
```
>The data contains some missing values, indicated by NaN.

To check how many NaN values are in each column, `df.isnull().sum()` is used.

```python
df.isnull().sum()
```

Output:

```
		0
id		0
name	1
class	1
mark	0
gender	2

dtype: int64
```
>From the output, the columns `name` and `class` each have one missing value, and `gender` has two missing values.

### 🧹  Cleaning missing values
Firstly, a new DataFrame was created with rows containing NaN values so that students can be identified and contacted to complete the information.

```python
df_missing = df[df.isnull().values.any(axis=1)]
print(df_missing)
```

Output:
```
    id      name  class  mark gender
8    9   Tes Qry    Six    78    NaN
14  15  Tade Row    NaN    88   male
26  27       NaN  Three    81    NaN
```

Drop rows with NaN values to ensure the DataFrame contains only complete records, and display the cleaned DataFrame.

```python
df = df.dropna()
print(df)
```
Output:

```
    id         name  class  mark  gender
0    1     John Deo   Four    75  female
1    2     Max Ruin  Three    85    male
2    3       Arnold  Three    55    male
3    4   Krish Star   Four    60  female
4    5    John Mike   Four    60  female
5    6    Alex John   Four    55    male
6    7  My John Rob  Fifth    78    male
7    8       Asruid   Five    85    male
9   10     Big John   Four    55  female
10  11       Ronald    Six    89  female
11  12        Recky    Six    94  female
12  13          Kty  Seven    88  female
13  14         Bigy  Seven    88  female
15  16        Gimmy   Four    88    male
16  17        Tumyu    Six    54    male
17  18        Honny   Five    75    male
18  19        Tinny   Nine    18    male
19  20       Jackly   Nine    65  female
20  21   Babby John   Four    69  female
21  22       Reggid  Seven    55  female
22  23        Herod  Eight    79    male
23  24    Tiddy Now  Seven    78    male
24  25     Giff Tow  Seven    88    male
25  26       Crelea  Seven    79    male
27  28    Rojj Base  Seven    86  female
28  29  Tess Played  Seven    55    male
29  30    Reppy Red    Six    79  female
30  31  Marry Toeey   Four    88    male
31  32    Binn Rott  Seven    90  female
32  33    Kenn Rein    Six    96  female
33  34     Gain Toe  Seven    69    male
34  35   Rows Noump    Six    88  female
```
To confirm that there are no NaN values in the DataFrame, `df.isnull().sum().sum()` is used.

```python
df.isnull().sum().sum()
```
Output:
```
np.int64(0)
```
>From the output `0`, we know there are no `NaN` values in the DataFrame, so it is ready for analysis.

### 📊  Analysing

Exploring the distribution of students by gender at the university using `value_counts()`.

```python
df['gender'].value_counts()
```
Output:
```
		count
gender	
female	16
male	16

dtype: int64
```
>The distribution shows there are an equal number of female and male students (16 each).

Average mark by gender:
```python
df.groupby('gender')['mark'].mean().round(0).astype(int)
```
Output:
```
		mark
gender	
female	77
male	71

dtype: float64
```
>Output shows that female students' marks are higher than male students' at the university.

Average mark by class and gender
```python
df.groupby(['class', 'gender'])['mark'].mean().round(0).astype(int)
```
Output:
```
	mark
class	gender	
Eight	male	79
Fifth	male	78
Five	male	80
Four	female	64
		male	77
Nine	female	65
		male	18
Seven	female	81
		male	74
Six		female	89
		male	54
Three	male	70

dtype: int64
```
>By analysing the data and calculating the average mark by class and gender, inconsistencies in the `class` column were identified: some values >are entered as adjectives (e.g., `fourth`, `fifth`) and some as words (e.g., `four`, `five`). Therefore, additional cleaning is needed to ensure >consistent values for each class.

```python
# DATA CLEANING - Standardise class names
# Replace ordinal words (third, fourth, …) with consistent number words (three, four, …)
df['class'] = df['class'].replace({
    'First': 'One',
    'Second': 'Two',
    'Third': 'Three',
    'Fourth': 'Four',
    'Fifth': 'Five',
    'Sixth': 'Six',
    'Seventh': 'Seven',
    'Eighth': 'Eight',
    'Ninth': 'Nine'
})
```
Average mark by class and gender (ordered from Three to Nine)

```python
class_order = ['Three','Four','Five','Six','Seven','Eight','Nine']
df['class'] = pd.Categorical(df['class'], categories=class_order, ordered=True)

df.groupby(['class','gender'], observed=True)['mark'].mean().round(0).astype(int)
```
Output:
```
		mark
class	gender	
Three	male	70
Four	female	64
male	77
Five	male	80
Six	female	89
male	54
Seven	female	81
male	74
Eight	male	79
Nine	female	65
male	18

dtype: int64
```









### 📈  Creating visualisations
List the charts you created and what insights they show.






## Results
Short summary of insights or outputs, e.g., charts, top students, trends.

## How to Run
Instructions to open the Jupyter Notebook and reproduce the analysis.

