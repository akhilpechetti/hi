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
def main1():
    tweet=st.text_input('tweet')
    if st.button('1'):
        vs = analyzer.polarity_scores(tweet)
        st.write("{}… {}".format(tweet[:30], str(vs)))

def main():
    CONSUMER_KEY = st.text_input('consumer key',3tDVUGFlwUAfrjtTNO6k1xfqW)
    CONSUMER_SECRET = st.text_input('sec',9I3BEaSP2LqS2wfQu0qXefJXDjUsqzouhoBvbDG6onv5VfU4lL)
    OAUTH_TOKEN = st.text_input('ctok',870901794452291584-zx8zAHDfvt9EdsCAAdNg9r5Se6GSiPP)
    OAUTH_TOKEN_SECRET = st.text_input('tok sec',RhOPigMTtITcw1c6O4L2wGg7qcgv7lqkzQpFpbFVyHM2e)
    username = st.text_input('username want to check')
    n=st.number_input('how many tweets',1,2000)
    if st.button('login'):
        auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
        api= tweepy.API(auth,wait_on_rate_limit=True)
        posts= api.user_timeline(screen_name='username',count=n,lang='en',tweet_mode='extended')
        st.write(posts[0:2])
if __name__ == '__main__':
        main()
