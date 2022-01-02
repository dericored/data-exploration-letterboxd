import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import rcParams

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

df = df['writer']
df = [item for sublist in df for item in sublist]
df = pd.DataFrame(df)
df.rename(columns={0:'Writer'}, inplace=True)
df = df.value_counts().reset_index(name='Movie Count')
df = df[df["Movie Count"] >= 2]
# df['Movie Count'] = df['Movie Count'].astype(int)

sns.set_theme()

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

plt.figure(figsize=[10,5])
fig = sns.barplot(data=df[:(10 if len(df)>10 else len(df))], x="Movie Count", y="Writer", color='powderblue')
plt.title('Top 10 Most Watched Writers '+r'$(n \geq 2)$', fontsize=15, y=1.05, loc="left")
fig.yaxis.labelpad = 25
fig.xaxis.set_major_locator(MaxNLocator(integer=True))
fig.bar_label(fig.containers[0], label_type='center', color='w', fontsize=11)

# save plot figure
plt.savefig("./results/14_writer_distribution.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)