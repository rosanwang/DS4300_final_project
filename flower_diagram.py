from pyplutchik import plutchik      # https://github.com/alfonsosemeraro/pyplutchik
import io
import pymongo
import base64
import matplotlib.pyplot as plt
from nrclex import NRCLex   # sentiment analysis

def get_emotions_text(text, keys):
    '''
    use NRCLex to obtain the emotion scores for a given text and list of emotions (i.e., keys)
    '''
    # Gets emotions associated to words in the review's text
    emo = NRCLex(text).raw_emotion_scores
    emo_filtered = {key: value for key, value in emo.items() if key in keys}

    return emo_filtered

def normalize_emotions(emotions):
    """
    Normalize emotion scores to a scale of 0-1
    """
    total = sum(emotions.values())
    return {k: v/total * 2.5 for k, v in emotions.items()}

def make_flower(input, year):
    """
    forms a flower visualization using pyplutchik package (https://github.com/alfonsosemeraro/pyplutchik)
    outputs the visualization as an image source
    """
    fig = plutchik(input, title=year)  # makes the flower diagram
    plt.savefig(year + ".png" ) # save the figure to the specified file
    plt.close()

def main():
    # Connecting to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["final_project"]
    collection = db["all_tweets"]
    # Defining and executing a query to obtain an aggregated list of tweets per year
    pipeline = [{'$project': {
            'tweet': 1,
            'year': {'$year': {'$dateFromString': {'dateString': '$date'}}}}},
    {'$group': {
            '_id': '$year',
            'tweets': {'$push': '$tweet'},
            'count': {'$sum': 1}}},
    {'$sort': {'_id': 1}}]

    results = list(collection.aggregate(pipeline))


    # keys for sentiment analysis
    emotions = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']

    for result in results:
        # define year and list of tweets
        year = result['_id']
        tweets = result['tweets']
        tweet_text = ' '.join(tweets)
        print("For year...", year)
        scores_dict = get_emotions_text(tweet_text, emotions)
        scores_dict = normalize_emotions(scores_dict)
        print(make_flower(scores_dict, str(year)))

main()
