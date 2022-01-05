# Letterboxd Data Exploration with Python

This project is inspired by Letterboxd's Year in Review stats, with some additional visualizations. To obtain the raw data, I scraped my personal diary (https://letterboxd.com/dericored/films/diary/) with Scrapy. Pandas and Matplotlib(+Seaborn) are used for data manipulation and visualization.

(_Note: this project is for educational purposes only_)

## Technologies

This project is created with:

- Scrapy 2.5.0
- Pandas 1.2.4
- Matplotlib 3.5.1
- Seaborn 0.11.1

## Data Exploration and Analysis

1.  **Basic stats**
    <!-- prettier-ignore -->
    <img src="./analysis/results/1_stats_text.png" width="250px">
    <img src="./analysis/results/2_additionalStats_text.png" width="250px">
2.  **Monthly and daily distribution**
    <!-- prettier-ignore -->
    <img src="./analysis/results/3_monthly_distribution_text.png" width="500px">
    <img src="./analysis/results/4_day_distribution.png" width="400px">

3.  **Top 10 genres, countries of origin, and languages**
    <!-- prettier-ignore -->
    <img src="./analysis/results/5_genre_distribution.png" width="400px">
    <img src="./analysis/results/6_country_distribution.png" width="400px">
    <img src="./analysis/results/7_language_distribution.png" width="400px">

4.  **Personal ratings distribution**
    <!-- prettier-ignore -->
    <img src="./analysis/results/8_ratings_distribution.png" width="400px">

5.  **Films liked and rewatched percentages**
    <!-- prettier-ignore -->
    <img src="./analysis/results/9_like_percent.png" width="250px">
    <img src="./analysis/results/10_rewatch_percent.png" width="250px">

6.  **Film runtime distribution**
    <!-- prettier-ignore -->
    <img src="./analysis/results/11_runtime_distribution.png" width="400px">

7.  **Top 10 directors, actors, writers and studios**
    <!-- prettier-ignore -->
    <img src="./analysis/results/12_director_distribution.png" width="400px">
    <img src="./analysis/results/13_actor_distribution.png" width="400px">
    <img src="./analysis/results/14_writer_distribution.png" width="400px">
    <img src="./analysis/results/15_studio_distribution.png" width="400px">

8.  **Highest and lowest audience ratings**
    <!-- prettier-ignore -->
    <img src="./analysis/results/16_highestAvgRating_table.png" width="400px">
    <img src="./analysis/results/17_lowestAvgRating_table.png" width="400px">

9.  **Largest differences (Personal ratings vs. Audience ratings)**
    <!-- prettier-ignore -->
    <img src="./analysis/results/18_ratingDifference_bar.png" width="750px">

10. **Genre combinations heatmap**
    <!-- prettier-ignore -->
    <img src="./analysis/results/19_genrePairs_heatmap.png" width="400px">

11. **Genre performances (selected, top 10)**
    <!-- prettier-ignore -->
    <img src="./analysis/results/20_genrePerformance_boxplot.png" width="700px">

12. **Longest movie marathon (consecutive days of watching films)**
    <!-- prettier-ignore -->
    <img src="./analysis/results/21_marathon_timeline_1.png" width="500px">
    <img src="./analysis/results/21_marathon_timeline_2.png" width="500px">

## How to Use

You can also use this project to analyze your own Letterboxd diary. To do that, follow the steps below.

1. Clone or download this repo.
2. Under `/letterboxd/spiders/`, find `diary_spider.py`. Change the username and time window accordingly.

   ```
   # change accordingly
   username = "dericored"
   period = ["2020/01/01", "2022/01/01"] # [from, to] in YYYY/MM/DD
   ```

3. Use the terminal. Go to the base directory and run,

   ```
   sh run.sh
   ```

4. You can find the generated figures in `/analysis/results/`.
