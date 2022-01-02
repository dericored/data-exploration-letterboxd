import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams    

# open file and store to df
f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')
df = pd.read_json(f)
df = pd.to_datetime(df['watch_date'])

# find total movies
total = len(df)

# find period (in months) between first and last record
months = (max(df).year - min(df).year)*12 + (max(df).month - min(df).month)

per_month = total/months

# find period (in weeks) between first and last record
weeks = (max(df) - min(df)).days//7

per_week = total/weeks

# configure fonts for plot
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

# plot stats as texts
plt.text(x=0.0, y=0.7, s='Films watched', va='center', ha='center', fontsize=15, color='gray')
plt.text(x=0.0, y=0.5, s=total, va='center', ha='center', fontsize=30, fontweight='semibold')
plt.text(x=0.5, y=0.7, s='Average per month', va='center', ha='center', fontsize=15, color='gray')
plt.text(x=0.5, y=0.5, s='{:.1f}'.format(per_month), va='center', ha='center', fontsize=30, fontweight='semibold')
plt.text(x=1.05, y=0.7, s='Average per week', va='center', ha='center', fontsize=15, color='gray')
plt.text(x=1.05, y=0.5, s='{:.1f}'.format(per_week), va='center', ha='center', fontsize=30, fontweight='semibold')
plt.text(x=0.5, y=0.25, s='from {}  ~  {}'.format(min(df).strftime('%B %d, %Y'), max(df).strftime('%B %d, %Y')), va='center', ha='center', fontsize=15, color='gray')
plt.axis('off')

# save plot figure
plt.savefig("./results/1_stats_text.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)

print("1_stats_text.png generated.")