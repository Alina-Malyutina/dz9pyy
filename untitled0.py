# -*- coding: utf-8 -*-
"""untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/Alina-Malyutina/3ce0fec8cf5e962e8d8f2aaf15962d7d/untitled0.ipynb
"""

import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

df.columns

df[(df['population'] >= 0) & (df['population'] <= 500)]['median_house_value'].mean()

df[df['households'] == df['households'].min()]['households'].max()