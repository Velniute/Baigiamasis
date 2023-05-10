import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


df = pd.read_csv('df_clean.csv')
# df.info()
# print(df.describe())

# #koks procentas NaN reiksmiu df
# print(df.isnull().sum() * 100/len(df))

# #kokios unikalios stulpeliu reiksmes
# print(df['Pavaru_dezes_tipas'].unique())

# #kiek yra 0 reiksmiu stulpeliuse
# print(df[df['Rida']==0])

# #pasiplotinam, kad apziureti duomenis grafiskai
# df['Metai'].plot(kind='hist', bins=60)

