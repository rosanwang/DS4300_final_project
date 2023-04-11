from pymongo import MongoClient
import csv

client = MongoClient()
db = client.ds4300

tweets = db.tweets

# clear database
tweets.delete_many({})

file = "tweets.csv"


with open(file, encoding="utf-8") as tweet_csv:
    tweetreader = csv.reader(tweet_csv, delimiter = ',')
    header = next(tweetreader)
    print("Importing tweets...")
    for row in tweetreader:
        tweet = {attribute:value for attribute, value in zip(header, row)}
        tweets.insert_one(tweet)
print(f"Import completed - {tweets.count_documents({})} tweet documents inserted")



