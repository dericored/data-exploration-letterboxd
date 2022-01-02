#!/bin/sh

cd letterboxd

scrapy crawl diary -O scraped.json

cd ../analysis

rm -r ./results/*

python 1_stats_text.py && python 2_additionalStats_text.py && python 3_monthly_distribution.py && python 4_day_distribution.py && python 5_genre_distribution.py && python 6_country_distribution.py && python 7_language_dist.py && python 8_ratings_distribution.py && python 9_like_percent.py && python 10_rewatch_percent.py && python 11_runtime_distribution.py && python 12_director_distribution.py && python 13_actor_distribution.py && python 14_writer_distribution.py && python 15_studio_distribution.py && python 16_highestAvgRatingTitle_table.py && python 17_lowestAvgRatingTitle_table.py && python 18_ratingDifference_bar.py && python 19_genrePairs_heatmap.py && python 20_genrePerformance_boxplot.py && python 21_marathon_timeline.py

echo "Process completed. You can check the results in webscraping-scrapy-letterboxd/analysis/results/ folder."

