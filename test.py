import pandas as pd

data = pd.read_csv('data/movies.csv', encoding='latin-1', sep='\t', usecols=['title', 'genres'], index_col='title')



print(data.loc['Toy Story (1995)'].values)