import numpy as np
import pickle
import pandas as pd
import json
import tweepy
#from flasgger import Swagger
import streamlit as st
import joblib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

from PIL import Image
def loading():
    print('started')
    CONSUMER_KEY = '3tDVUGFlwUAfrjtTNO6k1xfqW'
    CONSUMER_SECRET = '9I3BEaSP2LqS2wfQu0qXefJXDjUsqzouhoBvbDG6onv5VfU4lL'
    OAUTH_TOKEN = '870901794452291584-zx8zAHDfvt9EdsCAAdNg9r5Se6GSiPP'
    OAUTH_TOKEN_SECRET = 'RhOPigMTtITcw1c6O4L2wGg7qcgv7lqkzQpFpbFVyHM2e'
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    api= tweepy.API(auth,wait_on_rate_limit=True)
    print('end')
def main1():
    tweet=st.text_input('tweet')
    if st.button('1'):
        vs = analyzer.polarity_scores(tweet)
        st.write("{}… {}".format(tweet[:30], str(vs)))

def main2():
    st.title('file upload')
    menu=['dataset']
    choice=st.sidebar.selectbox('menu',menu)
    if choice=='dataset':
        st.subheader('dataset')
def main():
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    #analyzer = SentimentIntensityAnalyzer()
    import streamlit as st
    s1=st.text_input('tweet')
    vs = analyzer.polarity_scores(s1)
    st.write("{}… {}".format(s1[:30], str(vs)))
    import twitter
    CONSUMER_KEY = '3tDVUGFlwUAfrjtTNO6k1xfqW'
    CONSUMER_SECRET = '9I3BEaSP2LqS2wfQu0qXefJXDjUsqzouhoBvbDG6onv5VfU4lL'
    OAUTH_TOKEN = '870901794452291584-zx8zAHDfvt9EdsCAAdNg9r5Se6GSiPP'
    OAUTH_TOKEN_SECRET = 'RhOPigMTtITcw1c6O4L2wGg7qcgv7lqkzQpFpbFVyHM2e'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    count = 20
    query = "vaccine"
    tweets = twitter_api.search.tweets(q=query, count=count,lang='en',tweet_mode="extended")
    tweetsWithSent = []
    for t in tweets['statuses']:
       text = (t['full_text'])
       ps = analyzer.polarity_scores(text)
       tweetsWithSent.append({'text':text, 'compound':ps['compound']})
    st.write(tweetsWithSent)
if __name__ == '__main__':
    #cursor=tweepy.Cursor(api.user_timeline,id=user).items(10)
    main()
