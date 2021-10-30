import numpy as np
import pickle
import pandas as pd
import json
import tweepy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#from flasgger import Swagger
import streamlit as st
import joblib
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
st.set_option('deprecation.showPyplotGlobalUse', False)

from PIL import Image
def authe():
    global CONSUMER_KEY
    global CONSUMER_SECRET
    global OAUTH_TOKEN
    global OAUTH_TOKEN_SECRET
    CONSUMER_KEY = '3tDVUGFlwUAfrjtTNO6k1xfqW'
    CONSUMER_SECRET = '9I3BEaSP2LqS2wfQu0qXefJXDjUsqzouhoBvbDG6onv5VfU4lL'
    OAUTH_TOKEN = '870901794452291584-zx8zAHDfvt9EdsCAAdNg9r5Se6GSiPP'
    OAUTH_TOKEN_SECRET = 'RhOPigMTtITcw1c6O4L2wGg7qcgv7lqkzQpFpbFVyHM2e'
def creat():
    #CONSUMER_KEY = '3tDVUGFlwUAfrjtTNO6k1xfqW'
    #CONSUMER_SECRET = '9I3BEaSP2LqS2wfQu0qXefJXDjUsqzouhoBvbDG6onv5VfU4lL'
    #OAUTH_TOKEN = '870901794452291584-zx8zAHDfvt9EdsCAAdNg9r5Se6GSiPP'
    #OAUTH_TOKEN_SECRET = 'RhOPigMTtITcw1c6O4L2wGg7qcgv7lqkzQpFpbFVyHM2e'
    global df
    authe()
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    api= tweepy.API(auth,wait_on_rate_limit=True)
    username=st.text_input('username')
    count=st.number_input('no of tweets')
    n=st.slider('no.of tweets to display')
    posts= api.user_timeline(screen_name=username,count=count,tweet_mode='extended')
    i=1
    df=pd.DataFrame([tweet.full_text for tweet in posts], columns=['tweets'])
    for tweet in posts[0:n]:
        st.write(str(i)+')' + tweet.full_text+'\n')
        i=i+1
    st.dataframe(df)
    df['tweets']=df['tweets'].apply(clean)
    st.dataframe(df)
    df['compound']=df['tweets'].apply(sentiment)
    st.dataframe(df)
    wordcl()
    df['analysis']=df['compound'].apply(getanalysis)
    st.dataframe(df)
    
def clean(text):
    text=re.sub(r'@[A-Za-z0-9]+','',text)#remove mentions
    text=re.sub(r'#','',text)#remove hashtags
    text=re.sub(r'RT[\s]+','',text)#remove retweets
    text=re.sub(r'https?:\/\/\S+','',text)#remove links
    return text
def sentiment(text):
    ps=analyzer.polarity_scores(text)
    return ps['compound']
def wordcl():#wordcloud
    allwords=''.join([twts for twts in df['tweets']])
    wordcloud=WordCloud(width=500, height=300,random_state=21,max_font_size=119).generate(allwords)
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.show()
    st.pyplot()
def getanalysis(score):
    if score<0:
        return 'Negative'
    elif score==0:
        return 'Neutral'
    else:
        return 'Positive'
def main():
    import tweepy
    creat()
    
    
if __name__ == '__main__':
    #cursor=tweepy.Cursor(api.user_timeline,id=user).items(10)
    main()
