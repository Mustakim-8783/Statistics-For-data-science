# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 22:26:21 2024

@author: dell
"""

import pandas as pd 
df=pd.read_csv("C:/3-statistics/IPL IMB381IPL2013.csv")
df.head()

df.iloc[:5,:7]

set(df['AGE'])

set(df['T-RUNS'])

df['CAPTAINCY EXP'].unique()

df.iloc[:3,:21]

import pandas as pd
import numpy as np
#for spydersssss
df=pd.read_csv("income.csv",names=["name","income"],skiprows=[0])
df
#for jupiter notebook
df=pd.read_csv("C:/3-statistics/income.csv",names=["name","income"],skiprows=[0])
df

df.income.describe()

df.income.quantile(0.5) #minimum value

df.income.quantile(0.5, interpolation="lower")

df.income.quantile(0.4, interpolation="lower")

df.income.quantile(0.25,interpolation="lower")

df.income.quantile(1,interpolation="higher")

percentile_99=df.income.quantile(0.99)
percentile_99

df_no_outlier=df[df.income<=percentile_99]
percentile_99

df['income'][3]=np.NAN

df.income.mean()

df_new=df.fillna(df.income.mean())
df_new

df.describe()

df.income.quantile(0)

df.income.quantile(1)

df.income.quantile(0.25)

df.income.mean()


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plr 

df=pd.read_csv("C:/3-statistics/train.csv.csv")
df.head()
df['Age'].describe()

df['Age'].plot(kind='hist',bins=50)

df['Age'].plot(kind='kde')

df['Age'].skew()

df['Age'].plot(kind='box')

df.columns
df[df['Age']>65]

df['Age'].isnull().sum()/len(df['Age'])

df['Embarked'].value_counts()

df['Embarked'].value_counts().plot(kind='bar')

df['Embarked'].value_counts().plot(kind='pie',autopct='%0.1f%%')











