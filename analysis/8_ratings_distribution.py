import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

df = df['my_rating']
df = [str(rating) for rating in df]
df = pd.DataFrame(df)
df.rename(columns={0:'Ratings'}, inplace=True)

sns.set_theme()

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

fig = sns.catplot(x="Ratings",data=df, kind="count", order=[str(x) for x in np.arange(0.5,5.1,0.5)], color='orange', aspect=1.5)
plt.ylabel("Movie Count")
plt.title("Ratings Given (scale: 0.5 - 5.0)", fontsize=15, loc="left", y=1.05)
for ax in fig.axes.flatten():
    ax.bar_label(ax.containers[0], padding=3, label_type='center', color='w', fontsize=11)

# save plot figure
plt.savefig("./results/8_ratings_distribution.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)