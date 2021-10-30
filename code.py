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
def main():
    import tweepy
    CONSUMER_KEY = '3tDVUGFlwUAfrjtTNO6k1xfqW'
    CONSUMER_SECRET = '9I3BEaSP2LqS2wfQu0qXefJXDjUsqzouhoBvbDG6onv5VfU4lL'
    OAUTH_TOKEN = '870901794452291584-zx8zAHDfvt9EdsCAAdNg9r5Se6GSiPP'
    OAUTH_TOKEN_SECRET = 'RhOPigMTtITcw1c6O4L2wGg7qcgv7lqkzQpFpbFVyHM2e'
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    api= tweepy.API(auth,wait_on_rate_limit=True)
    username=st.text_input('username')
    posts= api.user_timeline(screen_name=username,count=10,tweet_mode='extended')
    i=1
    df=pd.DataFrame([tweet.full_text for tweet in posts], columns=['tweets'])
    for tweet in posts[0:5]:
        st.write(str(i)+')' + tweet.full_text+'\n')
        i=i+1
if __name__ == '__main__':
    #cursor=tweepy.Cursor(api.user_timeline,id=user).items(10)
    main()
