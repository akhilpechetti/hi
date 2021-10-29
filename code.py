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
    tweet=st.text_input('tweet')
    vs = analyzer.polarity_scores(tweet)
    print("{}… {}".format(s1[:30], str(vs)))

def main1():
    CONSUMER_KEY = st.text_input('consumer key')
    CONSUMER_SECRET = st.text_input('sec')
    OAUTH_TOKEN = st.text_input('ctok')
    OAUTH_TOKEN_SECRET = st.text_input('tok sec')
    username = st.text_input('username want to check')
    n=st.number_input('how many tweets',1,2000)
    if st.button('login'):
        auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
        api= tweepy.API(auth,wait_on_rate_limit=True)
        posts= api.user_timeline(screen_name='username',count=n,lang='en',tweet_mode='extended')
        print(posts[0:2])
if __name__ == '__main__':
        main()
