from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')
#print(df['release_year'].value_counts())

movies = df[df['type_id'] == 1]
shows = df[df['type_id'] == 2]

pelis = movies['release_year'].value_counts()
series = shows['release_year'].value_counts()

index =[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

df = pd.DataFrame({'Movies': pelis,
                   'Tv Shows': series}, index=index)

ax = df.plot.bar(rot=0)
plt.show()
