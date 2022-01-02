import pandas as pd
from pandas.api.types import CategoricalDtype
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

# define days
day = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_type = CategoricalDtype(categories=day, ordered=True)

# count occurences
df = df['watch_date']
df = pd.to_datetime(df)
df = df.dt.day_name()
df = df.astype(day_type)
df = df.value_counts(normalize=True).mul(100).round(1).reset_index(name='Movie Count').rename(columns={'index':'Day'})
df = df.sort_values('Day').reset_index(drop=True)

sns.set_theme()

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

plt.figure(figsize=[8,5])
fig = sns.barplot(data=df,x="Day", y="Movie Count", color='r')
plt.title("Weekly Activity on Letterboxd", fontsize=15, loc="left", y=1.05)
plt.xlabel("Day")
plt.ylabel("Watch Count (%)")
fig.bar_label(fig.containers[0], padding=3, color='grey', fontsize=11)

# save plot figure
plt.savefig("./results/4_day_distribution.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)

print("4_day_distribution.png generated.")