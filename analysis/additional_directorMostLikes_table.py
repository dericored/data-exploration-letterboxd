import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import six


f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

df = df[['director', 'like']]
df = df.explode('director')
df = df.value_counts().reset_index(name="Likes")
df = df[df['like'] == True]
df = df.rename(columns={'director': 'Director'}).reset_index(drop=True)
df = df.drop(columns=['like'])
df.index += 1
df = df[:3]

def render_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 2, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    mpl_table = ax.table(cellText=data.to_records(), bbox=bbox, colLabels=df.columns.insert(0, df.index.name), **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax

def max_widths(data):
    measurer = np.vectorize(len)
    max_lengths = measurer(data.to_numpy().astype(str)).max(axis=0)
    max_lengths = np.insert(max_lengths, 0, len(str(len(df))))
    
    i = 0
    for name in df.columns.insert(0, df.index.name):
        if len(str(name)) > max_lengths[i]: max_lengths[i] = len(str(name))
        i += 1

    return max_lengths

widths = max_widths(df)

ax = render_table(df, header_columns=0, col_width=sum(widths)/15, colWidths=widths, cellLoc='center', header_color="dimgray")
plt.title("Top 3 Directors with Most Likes", fontsize=15, y=1.05, loc='left')

plt.show()