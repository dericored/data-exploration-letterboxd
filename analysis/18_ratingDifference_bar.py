import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib.patches import FancyBboxPatch
from matplotlib.path import get_path_collection_extents

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

df = df[df['my_rating'] != 0]
df = df[['title', 'rating', 'my_rating']]
df['diff'] = df['my_rating'] - df['rating']
df = df.sort_values('diff', ascending=False)
df = pd.concat([df.head(10), df.tail(10)]).reset_index(drop=True)
df["vs. Avg Rating"] = np.where(df["diff"] > 0, "Higher", "Lower")
df = df.rename(columns={'title': 'Title', 'diff': 'Difference'})

sns.set_theme()

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

plt.figure(figsize=[12,10])
fig = sns.barplot(x="Difference", y="Title", data=df, hue="vs. Avg Rating", palette=['g','r'])
plt.title("Largest Rating Difference (Given Rating vs. Average Rating)", fontsize=15, y=1.05, loc='left')
fig.bar_label(fig.containers[0], color='w', fontsize=10, padding=5, label_type='center')
fig.bar_label(fig.containers[1], color='w', fontsize=10, padding=5, label_type='center')

for i,y in enumerate(fig.get_yticks()):
    if df["vs. Avg Rating"][i] == 'Higher': plt.annotate(round(df["rating"][i],2), (0.125*min(df["Difference"]),y-0.05), fontsize=10)
    else: plt.annotate(round(df["rating"][i],2), (-0.05*min(df["Difference"]),y+0.3), fontsize=10)

plt.annotate("Avg. Ratings", (0.5*min(df["Difference"]), 5))
plt.annotate("Avg. Ratings", (-0.3*min(df["Difference"]), 15))
        
# save plot figure
plt.savefig("./results/18_ratingDifference_bar.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)