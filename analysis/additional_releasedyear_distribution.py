import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

df = df['released_year']
df = df.sort_values().reset_index(drop=True)

sns.set_theme()

fig = sns.displot(data=df, aspect=2, color="tomato")

plt.title("Watch History by Released Year", fontsize=15, loc="left", y=1.05)
plt.xlabel("Released Year")
plt.ylabel("Movie Count")

plt.show(fig)
