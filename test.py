import tweepy

auth = tweepy.OAuth1UserHandler(
    "ueRXxydM3Vg3ppdbdKsdptjnL", "hhwbCTPKD3uAy6ikUBNsWhCWQ7lXPxUXjCRknysgkCpP9CUo8f"
)
api = tweepy.API(auth)
search_results = api.search_tweets("economy")

for i in search_results:
    print(i)
