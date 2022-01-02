import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

top_genres = df['genre']
top_genres = [item for sublist in top_genres for item in sublist]
top_genres = pd.DataFrame({'Genres': top_genres})
top_genres = top_genres.value_counts().reset_index(name='Movie Count')
top_genres = top_genres[:10]

df = df[df['my_rating'] != 0]
df = df[['title', 'genre', 'my_rating']]
df = df.explode('genre')
df = df[df['genre'].str.contains('|'.join(top_genres['Genres']))]
df = df.rename(columns={'genre': 'Genre', 'my_rating': 'Ratings'})

plt.figure(figsize=[15,5])

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

fig = sns.boxplot(data=df, x="Genre", y="Ratings", order=top_genres['Genres'], saturation=0.5, width=0.5, linewidth=0.8, fliersize=2)
plt.title("Genre Performances by Given Ratings", fontsize=15, y=1.05, loc='left')

# save plot figure
plt.savefig("./results/20_genrePerformance_boxplot.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)