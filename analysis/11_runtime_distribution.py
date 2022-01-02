import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

df = df['runtime']
df = df.sort_values().reset_index(drop=True)

sns.set_theme()

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

fig = sns.histplot(data=df, binwidth=20, binrange=[80,200], color="coral")
plt.title("Runtime Distribution of Watch History", fontsize=15, loc="left", y=1.05)
plt.xlabel("Runtime (min)")
plt.ylabel("Movie Count")
fig.bar_label(fig.containers[0], padding=3, fontsize=11, color='grey')

# save plot figure
plt.savefig("./results/11_runtime_distribution.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)