import twint
import datetime

# for some reason only tweets from 2007-03-01 onwards exist
for year in range(2008, 2023):
    for month in range(1, 12):
        since = datetime.datetime(year, month, 1)
        until = datetime.datetime(year, month + 1, 1)

        c = twint.Config()
        c.Search = "economy OR recession OR stock OR inflation OR economic growth OR employment"
        c.Min_likes = 100
        c.Limit = 100
        c.Store_csv = True
        c.Output = "tweets.csv"
        c.Since = str(since)
        c.Hide_output = True
        c.Until = str(until)
        print(since)
        print(until)
        twint.run.Search(c)


