import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


def plot_continuous_distribution(data: pd.DataFrame = None, column: str = None, hue=None ,height: int = 8):
    _ = sns.displot(data, x=column, hue=hue ,kde=True, height=height, aspect=height/5).set(title=f'Distribution of {column}')
 
def get_unique_values(data:pd.DataFrame=None, column:str=None, unique_values:str=None):
    """this methods returns the number of counts in percentage"""
    num_unique_values = data[column].nunique()
    
    percent_count = data[column].value_counts(normalize=True)*100
    
    print(f"Column: {column} has {num_unique_values} unique values\n")
    print("{}".format(percent_count))
    
    if unique_values == 'show':
        print(f"unique values :- {data[column].unique()}")


def plot_categorical_distribution(data: pd.DataFrame = None, column: str = None, hue:str=None, height: int = 8, aspect: int = 2):
    
    if hue:
        turnover = data.groupby(column)[hue].value_counts(normalize=True).mul(100)
        
        _ = sns.countplot(data = data, x=column, hue=hue)

        
        return turnover
    else: 
        _ = sns.catplot(data=data, x=column, kind='count', height=height, aspect=aspect).set(title=f'Distribution of {column}')
          
def correlation_plot(data: pd.DataFrame = None):
    corr = df.corr()
    corr.style.background_gradient(cmap='coolwarm')
    
    
## skewness of the data
def skewed(data:pd.DataFrame=None, column:str=None):
    skewness = data[column].skew()
    mean = data[column].mean()
    median = data[column].median()
    print(f"Skewness for column {column}")
    print('mean :', mean)
    print('median :', median)
    
    if mean > median:
        print(f"Right skewd Distribution mean is to the right of column {column}\nskewness > 1\n",skewness)
    elif mean < median:
        print("Left skewd Distribution mean is to the Left of column {column}\nskewness < 1\n",skewness)
    else:
        print(f"Distribution is Normal of column {column} {mean, median} are equal", 'skewness =', skewness)






def plot_continuous_distribution_and_skewness(data: pd.DataFrame = None, column: str = None, hue=None ,height: int = 8):
    
    skewness = data[column].skew()
    mean = data[column].mean()
    median = data[column].median()
    print('mean :', mean)
    print('median :', median)
    
    if mean > median:
        print(f"Right skewd Distribution mean is to the right of column {column}\nskewness > 1\n",skewness)
        _ = sns.displot(data, x=column, hue=hue ,kde=True, height=height, aspect=height/5).set(title=f'Distribution of {column}')
        return _
    
    elif mean < median:
        print("Left skewd Distribution mean is to the Left of column {column}\nskewness < 1\n",skewness)
        _ = sns.displot(data, x=column, hue=hue ,kde=True, height=height, aspect=height/5).set(title=f'Distribution of {column}')
        return _
    
   
    else:
        print(f"Distribution is Normal of column {column} {mean, median} are equal", 'skewness =', skewness)
        _ = sns.displot(data, x=column, hue=hue ,kde=True, height=height, aspect=height/5).set(title=f'Distribution of {column}')
        return _
    
# def skewed(data:pd.DataFrame=None, column:str=None):
#     skewness = data[column].skew()
#     mean = data[column].mean()
#     median = data[column].median()
#     print('mean :', mean)
#     print('median :', median)
#     
#     if mean > median:
#         print("Right skewd Distribution mean is to the right\nskewness > 1\n",skewness)
#     elif mean < median:
#         print("Left skewd Distribution mean is to the Left\nskewness < 1\n",skewness)
#     else:
#         print(f"Distribution is Normal {mean, median} are equal", 'skewness =', skewness)