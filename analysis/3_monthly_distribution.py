import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams  


f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

# get year-month information
dates = df['watch_date']
dates = pd.to_datetime(dates)
dates = dates.dt.strftime('%Y-%m')

# count occurences
dates_count =  pd.DataFrame(pd.date_range(min(dates), max(dates), freq='MS'), columns=['Month'])
dates_count['Month'] = dates_count['Month'].dt.strftime('%Y-%m')
dates_count['Count'] = 0

dates = dates.value_counts()

# sort months
for month in dates.index:
    match_index = dates_count.loc[dates_count['Month'] == month].index[0]
    dates_count.iloc[match_index, 1] = dates[month]


sns.set_theme()
plt.figure(figsize=[12+2,5])

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Verdana']

fig = sns.barplot(data=dates_count[len(dates_count)-12:], x='Month', y='Count', color='b', dodge=False)
plt.title("Monthly Activity on Letterboxd (Last 12 Months)", fontsize=15, loc="left", y=1.05)
plt.xlabel("Month")
plt.ylabel("Watch Count")
fig.bar_label(fig.containers[0], padding=3, fontsize=11, color='grey')

# save plot figure
plt.savefig("./results/3_monthly_distribution_text.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)

print("3_monthly_distribution_text.png generated.")