import pandas as pd

data = pd.read_csv('data/movies.csv', encoding='latin-1', sep='\t')



data = data[['title', 'genres']]
data['genres'] = data['genres'].apply(lambda x : x.replace('|', ' '))
