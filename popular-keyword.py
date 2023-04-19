import twint
import datetime


# can only fetch last 3200 tweets
for year in range(2008, 2023):
    for month in range(1, 12):
        since = datetime.datetime(year, month, 1)
        until = datetime.datetime(year, month + 1, 1)

        c = twint.Config()
        c.Min_likes = 100
        c.Limit = 75
        c.Search = "expensive OR cheap"
        c.Store_csv = True
        c.Output = "popular_expensive_cheap_tweets_v2.csv"
        c.Since = str(since)
        #c.Hide_output = True
        c.Until = str(until)
        print(since)
        print(until)
        twint.run.Search(c)
