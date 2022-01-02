import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams  

# open file and store to df
f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')
df = pd.read_json(f)

# store column data to respective variables
director = df['director']
actor = df['actor']
country = df['country']
runtime = df['runtime']
released_year = df['released_year']

# explode the list and get the number of unique directors, actors and countries
directors = director.explode().nunique()
actors = actor.explode().nunique()
countries = country.explode().nunique()

# get total runtime
total_runtime = sum(runtime)

# get the earliest and latest released year
earliest = min(released_year)
latest = max(released_year)

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

# plot stats as texts
plt.text(x=0.85, y=0.95, s='Stats', va='center', ha='right', fontsize=15, color='gray')
plt.text(x=0.15, y=0.75, s='Directors', va='center', ha='left', fontsize=15, color='gray')
plt.text(x=0.85, y=0.75, s=f'{directors:,}', va='center', ha='right', fontsize=25, fontweight='semibold')
plt.text(x=0.15, y=0.6, s='Actors', va='center', ha='left', fontsize=15, color='gray')
plt.text(x=0.85, y=0.6, s=f'{actors:,}', va='center', ha='right', fontsize=25, fontweight='semibold')
plt.text(x=0.15, y=0.45, s='Countries', va='center', ha='left', fontsize=15, color='gray')
plt.text(x=0.85, y=0.45, s=f'{countries:,}', va='center', ha='right', fontsize=25, fontweight='semibold')
plt.text(x=0.15, y=0.3, s='Runtime (mins)', va='center', ha='left', fontsize=15, color='gray')
plt.text(x=0.85, y=0.3, s=f'{total_runtime:,}', va='center', ha='right', fontsize=25, fontweight='semibold')
plt.text(x=0.15, y=0.1, s=f'from films released in {earliest} - {latest}', va='center', ha='left', fontsize=15, color='gray', fontweight='semibold')
plt.axis('off')

# save plot figure
plt.savefig("./results/2_additionalStats_text.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)

print("2_additionalStats_text.png generated.")