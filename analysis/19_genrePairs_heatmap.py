import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import product
import numpy as np
from matplotlib import rcParams

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

top_genres = df['genre']
top_genres = [item for sublist in top_genres for item in sublist]
top_genres = pd.DataFrame({'Genres': top_genres})
top_genres = top_genres.value_counts().reset_index(name='Movie Count')
top_genres = top_genres[:10]

table = pd.DataFrame(product(top_genres['Genres'], top_genres['Genres']))
table = table.rename(columns={0: 'Genre-1', 1:'Genre-2'})
table['count'] = 0

df = df['genre']

# count occurences
for i in range(len(table)):
    for j in range(len(df)):
        if set([table.iloc[i,0],table.iloc[i,1]]).issubset(df[j]) and table.iloc[i,0]!=table.iloc[i,1]: table.iloc[i,2] += 1

# apply pivot and filter out duplicates
pivot = table.pivot("Genre-1", "Genre-2", "count")
pivot = pivot.where(np.triu(np.ones(pivot.shape), k=1).astype(bool))

sns.set_theme()

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

sns.heatmap(pivot, cmap="YlOrRd", annot=True, cbar=False)
plt.title("Most Frequently Watched Genre Pairs", fontsize=15, y=1.05, loc='left')

# save plot figure
plt.savefig("./results/19_genrePairs_heatmap.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)

print("19_genrePairs_heatmap.png generated.")