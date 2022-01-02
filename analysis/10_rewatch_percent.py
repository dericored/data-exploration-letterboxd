import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

df = df['rewatch']
total = len(df)
df = df.value_counts().reset_index(name='Movie Count').rename(columns={'index':'Rewatch'})
if len(df)==1 and df.loc[0, "Rewatch"]==False: df.loc[1] = [True, 0]
if len(df)==1 and df.loc[0, "Rewatch"]==True: df.loc[1] = [False, 0]
df = df.sort_values('Rewatch', ascending=False)

plt.style.use('ggplot')

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

labels = 'Rewatch', 'First Watch'
plt.pie(data=df, x="Movie Count", autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, total*p/100), colors=['limegreen','gainsboro'], labels=labels)
plt.title("Proportion of Rewatches", fontsize=15, y=1.05, loc="left")

# save plot figure
plt.savefig("./results/10_rewatch_percent.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)