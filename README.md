# DS4300_final_project
## Studying Economic Sentiment
### What is the relationship between economic sentiment and real measurements of the economy? 
#### According to the Federal Reserve, inflation expectations play a significant role in determining inflation.1 Consumer sentiment influences investment decisions, which in turn influences economic conditions and outcomes. For example, if consumers are optimistic about the future, they are more likely to invest and consume, which boosts the economy. In many ways, economic conditions can be a self-fulfilling prophecy. If consumers believe recession is coming, they will reduce their spending which in turn will eventually lead to recession-like conditions.
---
### Dependencies: PyMongo, PySpark, Twint 
---
## Metadata 
### data  
- cpi-raw.csv: 2006-2023 consumer price index values (indicator of real inflation) 
- popular_price_tweets_v2.csv: tweets from 2008-2023 with the keyword 'expensive' or 'cheap' (min likes = 100) 
- popular_tweets.csv: tweets from 2008-2023 with the keywords related to "economy" (min likes = 100) 
- tweets.csv: tweets from 2008-2023 with the keywords related to "economy" (no minimum likes) 

### data_collection_files 
- supporting code to obtain the csv files using Twint 
---
### Analysis 
- sentiment_analysis.ipynb: conducts sentiment analysis via VADER library 
- cpi_sentiment.ipynb: conducts analysis using cpi data to visualize relationship between cpi and sentiment 
- words_analysis.ipynb: looks at tweets with keywords "cheap" and "expensive"; analysis on words most associated with 'expensive' 
- yearly_correlation_analysis_spark.ipynb: looks into correlation between inflation and sentiment over time  
