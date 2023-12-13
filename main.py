#pip install ntscraper
#pip install pandas
#pip install tqdm

from ntscraper import Nitter
import pandas as pd

def sc(username , mode, number ):
    scraper = Nitter()
    tweets  = scraper.get_tweets(username , mode=mode , number=number )
    tweet_list = []
    for tw in tweets['tweets']:
        tweet_list.append([tw['text'] , tw['date']])
    df = pd.DataFrame(tweet_list , columns=['text' , 'date'])
    print(df)
    df.to_csv('user.csv')

sc('dley_mr' , mode='user' , number=10 )


