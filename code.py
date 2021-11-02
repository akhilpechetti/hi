from PIL import Image
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


def load_saved_artifacts():
    #print("loading saved artifacts...start")
    global __model
    __model=None
    if __model is None:
        with open('classification1.joblib', 'rb') as f:
            __model = joblib.load(f)
    #print("loading saved artifacts...done")


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
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    username = st.text_input('username')
    count = st.number_input('no of tweets')
    n = st.slider('no.of tweets to display for top for an overview')
    posts = api.user_timeline(screen_name=username,
                              count=count, tweet_mode='extended')
    i = 1
    df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['tweets'])
    df['tweets'] = df['tweets'].apply(clean)
    global scores_df
    scores_df = df.copy()
    for tweet in posts[0:n]:
        st.write(str(i)+')' + tweet.full_text+'\n')
        i = i+1
    # st.header('Dataset')
    if st.button('view dataset'):
        st.dataframe(df)
    # st.dataframe(df)
    df['tweets'] = df['tweets'].apply(clean)
    # st.dataframe(df)
    scores_df['score'] = scores_df['tweets'].apply(sentiment)
    if st.button('dataset wth scores'):
        st.dataframe(scores_df)
    global analysis_df
    analysis_df = scores_df.copy()
    # st.dataframe(df)
    analysis_df['analysis'] = analysis_df['score'].apply(getanalysis)
    if st.button('dataset containing positive or negative tweet or neutral tweet'):
        st.dataframe(analysis_df)
    # st.dataframe(df)
    if st.button('wordcloud image of most used words'):
        wordcl()
    menu = ['None', 'positive tweet percent',
            'negative tweet percent', 'neutral tweet percent']
    choice = st.selectbox(
        'percent of different tweets based on sentiment', menu)
    if choice == 'positive tweet percent':
        postive_percent()
    if choice == 'negative tweet percent':
        negative_percent()
    if choice == 'neutral tweet percent':
        neutral_percent()
    menu1 = ['None', 'positive tweets', 'negative tweets', 'neutral tweets']
    choice1 = st.selectbox('View positive, negative or neutral tweets', menu1)
    if choice1 == 'positive tweets':
        postive_tweets()
    if choice1 == 'negative tweets':
        negative_tweets()
    if choice1 == 'neutral tweets':
        neutral_tweets()
    # postive_tweets()
    # postive_percent()
    # value_coun()
    if st.button('sentiment vs no.of tweets graph'):
        value_coun_graph()
    global ak_df
    ak_df = df.copy()
    ak_df['catogery']=ak_df['tweets'].apply(catogery)
    if st.button('view different categories of Tweets in Dataset'):
        st.dataframe(ak_df)
    menu1 = ['None', 'Sports related', 'Business related', 'Entertainment related','Politics related','Tech related']
    choice1 = st.selectbox('view different categories of Tweets', menu1)
    if choice1 == 'Sports related':
        sports_tweets()
    if choice1 == 'Business related':
        business_tweets()
    if choice1 == 'Entertainment related':
        entertainment_tweets()
    if choice1 == 'Politics related':
        politic_tweets()
    if choice1 == 'Tech related':
        tech_tweets()


def catogery(text):
    text=pd.Series(data=text)
    return __model.predict(text)


def clean(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # remove mentions
    text = re.sub(r'#', '', text)  # remove hashtags
    text = re.sub(r'RT[\s]+', '', text)  # remove retweets
    text = re.sub(r'https?:\/\/\S+', '', text)  # remove links
    return text


def sentiment(text):
    ps = analyzer.polarity_scores(text)
    return ps['compound']


def wordcl():  # wordcloud
    allwords = ''.join([twts for twts in df['tweets']])
    wordcloud = WordCloud(width=500, height=300, random_state=21,
                          max_font_size=119).generate(allwords)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    st.pyplot()


def getanalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'
def sports_tweets():
    st.header('sports tweets')
    j = 1
    for i in range(0, ak_df.shape[0]):
        if(ak_df['catogery'][i] == 'sport'):
            st.write(str(j)+')'+ak_df['tweets'][i]+'\n')
            j = j+1
def business_tweets():
    st.header('business tweets')
    j = 1
    for i in range(0, ak_df.shape[0]):
        if(ak_df['catogery'][i] == 'business'):
            st.write(str(j)+')'+ak_df['tweets'][i]+'\n')
            j = j+1
def entertainment_tweets():
    st.header('entertainment tweets')
    j = 1
    for i in range(0, ak_df.shape[0]):
        if(ak_df['catogery'][i] == 'entertainment'):
            st.write(str(j)+')'+ak_df['tweets'][i]+'\n')
            j = j+1
def politic_tweets():
    st.header('political tweets')
    j = 1
    for i in range(0, ak_df.shape[0]):
        if(ak_df['catogery'][i] == 'politics'):
            st.write(str(j)+')'+ak_df['tweets'][i]+'\n')
            j = j+1
def tech_tweets():
    st.header('Tech tweets')
    j = 1
    for i in range(0, ak_df.shape[0]):
        if(ak_df['catogery'][i] == 'tech'):
            st.write(str(j)+')'+ak_df['tweets'][i]+'\n')
            j = j+1


def postive_tweets():
    st.header('postive tweets')
    j = 1
    sortedDF = analysis_df.sort_values(by=['score'])
    for i in range(0, sortedDF.shape[0]):
        if(sortedDF['analysis'][i] == 'Positive'):
            st.write(str(j)+')'+sortedDF['tweets'][i]+'\n')
            j = j+1


def negative_tweets():
    st.header('Negative tweets')
    j = 1
    sortedDF = analysis_df.sort_values(by=['score'], ascending=False)
    for i in range(0, sortedDF.shape[0]):
        if(sortedDF['analysis'][i] == 'Negative'):
            st.write(str(j)+')'+sortedDF['tweets'][i]+'\n')
            j = j+1


def neutral_tweets():
    st.header('Neutral tweets')
    j = 1
    sortedDF = analysis_df.sort_values(by=['score'], ascending=False)
    for i in range(0, sortedDF.shape[0]):
        if(sortedDF['analysis'][i] == 'Neutral'):
            st.write(str(j)+')'+sortedDF['tweets'][i]+'\n')
            j = j+1


def postive_percent():
    req_tweets = analysis_df[analysis_df.analysis == 'Positive']
    req_tweets = req_tweets['tweets']
    st.header('Postive tweets percent')
    st.write(round((req_tweets.shape[0]/df.shape[0])*100, 1))


def negative_percent():
    req_tweets = analysis_df[analysis_df.analysis == 'Negative']
    req_tweets = req_tweets['tweets']
    st.header('Negative tweets percent')
    st.write(round((req_tweets.shape[0]/df.shape[0])*100, 1))


def neutral_percent():
    req_tweets = analysis_df[analysis_df.analysis == 'Neutral']
    req_tweets = req_tweets['tweets']
    st.header('Neutral tweets percent')
    st.write(round((req_tweets.shape[0]/df.shape[0])*100, 1))


def value_coun_graph():
    analysis_df['analysis'].value_counts()
    plt.title('sentment analysis')
    plt.xlabel('sentiment')
    plt.ylabel('counts')
    analysis_df['analysis'].value_counts().plot(kind='bar')
    plt.show()
    st.pyplot()


def main():
    import tweepy
    creat()


if __name__ == '__main__':
    # cursor=tweepy.Cursor(api.user_timeline,id=user).items(10)
    load_saved_artifacts()
    main()
