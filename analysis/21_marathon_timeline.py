import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from matplotlib import rcParams

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

df = df[['watch_date','title']]
df['watch_date'] = pd.to_datetime(df['watch_date'])
df = df.sort_values('watch_date').reset_index(drop=True)

# count consecutive days
y = df['watch_date']
x = y.groupby((y != y.shift() + pd.DateOffset(1)).cumsum()).cumcount() + 1

df['consecutives'] = x
max_consecutives = max(df['consecutives'])
endpoints = df[df['consecutives'] == max_consecutives]

consecutives = []
for end in endpoints.index.values:
    start = end - max_consecutives + 1
    timeline = pd.DataFrame(df[start:end+1])
    consecutives.append(timeline)
    
# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

for i in range(len(consecutives)):
    data = consecutives[i]
    title = data['title'].tolist()
    dates = data['watch_date'].tolist()

    # Choose some nice levels
    levels = np.tile([-5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(dates)/6)))[:len(dates)]

    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize=(len(data)/1.1, 4), constrained_layout=True)
    plt.rcParams['figure.facecolor'] = 'w'
    plt.suptitle("Longest Movie Marathon", fontsize=15, y=1.1, ha='right', x=1)
    plt.title("{} - {} ({} days)".format(dates[0].strftime('%B %d, %Y'), dates[-1].strftime('%B %d, %Y'), len(data)), fontsize=12, y=1.025, loc='left')

    ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
    ax.plot(dates, np.zeros_like(dates), "-o",
            color="k", markerfacecolor="w")  # Baseline and markers on it.

    # annotate lines
    j = 0
    for d, l, r in zip(dates, levels, title):
        if len(r) > 20: r = r[:20] + '...'
        ax.annotate(r, xy=(d, l),
                    xytext=(0, np.sign(l)*3), textcoords="offset points",
                    horizontalalignment="left" if j<len(data)/2 else "right",
                    verticalalignment="bottom" if l > 0 else "top")
        j += 1

    # format xaxis
    ax.set_xticks([date for date in [dates[0],dates[len(data)//2],dates[-1]]])
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d, %Y"))

    # remove y axis and spines
    ax.yaxis.set_visible(False)

    ax.margins(y=0.1)
    
    # save plot figure
    plt.savefig(f"./results/21_marathon_timeline_{i+1}.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)

    print(f"21_marathon_timeline_{i+1}.png generated.")