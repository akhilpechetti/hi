import numpy as np
import pickle
import pandas as pd
import json
import tweepy
#from flasgger import Swagger
import streamlit as st
import joblib

from PIL import Image

def main():
    CONSUMER_KEY = st.text_input('consumer key')
    CONSUMER_SECRET = st.text_input('consumer secret')
    OAUTH_TOKEN = st.text_input('oauth token')
    OAUTH_TOKEN_SECRET = st.text_input('oauth token secret')
    username = st.text_input('username want to check')
    n=st.number_input('how many tweets',1,2000)
    if st.button('login'):
        global posts
        auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
        api= tweepy.API(auth,wait_on_rate_limit=True)
        posts= api.user_timeline(screen_name=username,count=n,tweet_mode='extended')
        st.success('logged in')
        st.button('n recent tweets')
            m=st.number_input('number',1,2000)
            i=1
            for tweet in posts[0:m]:
                print(str(i)+')' + tweet.full_text+'\n')
                    i=i+1
if __name__ == '__main__':
    main()
 
