import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pandas.api.types import CategoricalDtype


f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

df = df[['released_year','my_rating']]

df['my_rating'] = [str(rating) for rating in df['my_rating']]
rating_order = [str(x) for x in np.arange(0.5,5.1,0.5)]
rating_type = CategoricalDtype(categories=rating_order, ordered=True)
df['my_rating'] = df['my_rating'].astype(rating_type)
df["Century"] = np.where(df["released_year"] > 1999, "21st Century", "20th Century")
df = df.rename(columns={'my_rating': 'Given Ratings'})

sns.set_theme()

fig = sns.displot(data=df, x="Given Ratings", hue="Century", kde=True)
plt.title("Distribution of Given Ratings, Grouped by Century", fontsize=15, y=1.05, loc='left')