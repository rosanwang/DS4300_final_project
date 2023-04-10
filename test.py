import tweepy
import csv

auth = tweepy.OAuth1UserHandler(
    "ueRXxydM3Vg3ppdbdKsdptjnL", "hhwbCTPKD3uAy6ikUBNsWhCWQ7lXPxUXjCRknysgkCpP9CUo8f"
)
api = tweepy.API(auth)
search_results = api.search_tweets("economy")

# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)
#print(search_results)

for tweet in search_results:
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print(tweet.created_at, tweet.text)

csvFile.close()
# Write a row to the CSV file. I use encode UTF-8

    #print(i)

#curl "https://api.twitter.com/1.1/tweets/search/fullarchive/test/counts.json?query=TwitterDev%20%5C%22search%20api%5C%22" -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAIbkmAEAAAAAPqZjYeHTfgNyJM0b0%2BdEwWKZgI4%3DE9bngHR8cyR6lUsOf98ivqfy9T2JNVxY1g0F3U9BNIXKLMvSJB"
#curl https://api.twitter.com/2/tweets/search/recent?query=cat%20has%3Amedia%20-grumpy&max_results=100 -H "Authorization: Bearer $BEARER_TOKEN"
#curl "https://api.twitter.com/2/tweets/search/fullarchive/test/counts.json?query=cat&max_results=100>" -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAIbkmAEAAAAAPqZjYeHTfgNyJM0b0%2BdEwWKZgI4%3DE9bngHR8cyR6lUsOf98ivqfy9T2JNVxY1g0F3U9BNIXKLMvSJB"