import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import MaxNLocator

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

# count occurences
df = df['actor']
df = [item for sublist in df for item in sublist] # deconstruct object inside object in json
df = pd.DataFrame(df)
df.rename(columns={0:'Actor'}, inplace=True)
df = df.value_counts().reset_index(name='Movie Count')
df = df[df["Movie Count"] >= 2]

sns.set_theme()

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

plt.figure(figsize=[10,5])
fig = sns.barplot(data=df[:(10 if len(df)>10 else len(df))], x="Movie Count", y="Actor", color='gold')
plt.title('Top 10 Most Watched Actors '+r'$(n \geq 2)$', fontsize=15, y=1.05, loc="left")
fig.yaxis.labelpad = 25
fig.xaxis.set_major_locator(MaxNLocator(integer=True))
fig.bar_label(fig.containers[0], label_type='center', color='w', fontsize=11)

# save plot figure
plt.savefig("./results/13_actor_distribution.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)