# -*- coding: utf-8 -*-
"""zomato data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11WIvjkLd_nHI54u2-TeDBtlGADRP8Csg

Importing the required Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""Loading the file"""

df = pd.read_csv('zomato (1).csv')
df_code=pd.read_excel('Country-Code.xlsx')
df.head()

#to determine the shape of the file
df.shape

df.columns

df = df.drop(['Restaurant ID','Address','Locality', 'Locality Verbose', 'Longitude', 'Latitude'],axis=1)
#drop unwanted data

df.head()

df.info()
#to view the summary of the file

df.drop_duplicates(inplace = True)
df.shape

df['Cuisines'].unique

df.describe()

sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')

sns.heatmap(df.corr(),
            annot=True,
            linewidths=1)

df.isnull().sum()
#to see all null/Na data

df.isna().sum()

final_df=pd.merge(df,df_code,on='Country Code', how='left')
final_df.head(2)

final_df.columns

country_names=final_df.Country.value_counts().index

country_val=final_df.Country.value_counts().values

plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')

ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})

ratings

"""Observation
When Rating is between 4.5 to 4.9---> Excellent
When Rating are between 4.0 to 3.4--->very good
when Rating is between 3.5 to 3.9----> good
when Rating is between 3.0 to 3.4----> average
when Rating is between 2.5 to 2.9----> average
when Rating is between 2.0 to 2.4----> Poor
"""

ratings.head()

import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Aggregate rating",y="Rating Count",data=ratings)

sns.barplot(x="Aggregate rating",y="Rating Count",hue='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])

sns.countplot(x="Rating color",data=ratings,palette=['blue','red','orange','yellow','green','green'])

final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()

final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)

final_df[final_df['Has Online delivery'] =="Yes"].Country.value_counts()

final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()

final_df.City.value_counts().index

city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index

plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')

