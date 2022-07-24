import tweepy
import configparser
import pandas as pd 
from flask import Flask, render_template, request
from datetime import datetime 

app = Flask(__name__)
# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication 
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# print(df)
# print(data)

# df.to_csv('romano.csv')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/displayTweets', methods = ['POST'])
def displayTweets():
    # user = ['FabrizioRomano', 'DiMarzio', 'JPercyTelegraph', 'bbcsport_david', 'TelegraphDucker', 'MarkOgden_', 'garyjacob', '_ChrisBascombe', 'simonpeach', 'ed_aarons']
    if request.method == 'POST':
        # print('tarun')
        user = request.form['twitterAcc']
        columns = ['', 'Tweet', 'Time']
        data = []
        # print(f'{user}')
        limit = 20

        def newDate(date):
            newformat = f"%dth %b %Y at %I:%M %p" 
            newdate =  datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S%z')
            return datetime.strftime(newdate, newformat)

        if user == 'FabrizioRomano':
            tweetsFabrizio = tweepy.Cursor(api.user_timeline, screen_name = user, count = 200, tweet_mode = 'extended').items(limit)

            for tweet in tweetsFabrizio:
                data.append([tweet.full_text, newDate(tweet.created_at)])

        elif user == 'DiMarzio':
            tweetsMarzio = tweepy.Cursor(api.user_timeline, screen_name = user, count = 200, tweet_mode = 'extended').items(limit)   

            for tweet in tweetsMarzio:
                data.append([tweet.full_text, newDate(tweet.created_at)])

        elif user == 'JPercyTelegraph':
            tweetsJpercy = tweepy.Cursor(api.user_timeline, screen_name = user, count = 200, tweet_mode = 'extended').items(limit) 

            for tweet in tweetsJpercy:
                data.append([tweet.full_text, newDate(tweet.created_at)])

        elif user == 'bbcsport_david':
            tweetsDavid = tweepy.Cursor(api.user_timeline, screen_name = user, count = 200, tweet_mode = 'extended').items(limit) 

            for tweet in tweetsDavid:
                data.append([tweet.full_text, newDate(tweet.created_at)])

        elif user == 'TelegraphDucker':
            tweetsDucker = tweepy.Cursor(api.user_timeline, screen_name = user, count = 200, tweet_mode = 'extended').items(limit) 

            for tweet in tweetsDucker:
                data.append([tweet.full_text, newDate(tweet.created_at)])

        elif user == 'MarkOgden_':
            tweetsOgden = tweepy.Cursor(api.user_timeline, screen_name = user, count = 200, tweet_mode = 'extended').items(limit) 

            for tweet in tweetsOgden:
                data.append([tweet.full_text, newDate(tweet.created_at)])

        elif user == 'garyjacob':
            tweetsJacob = tweepy.Cursor(api.user_timeline, screen_name = user, count = 200, tweet_mode = 'extended').items(limit) 
             
            for tweet in tweetsJacob:
                data.append([tweet.full_text, newDate(tweet.created_at)])

        elif user == '_ChrisBascombe':
            tweetsBascombe = tweepy.Cursor(api.user_timeline, screen_name = user, count = 200, tweet_mode = 'extended').items(limit)

            for tweet in tweetsBascombe:
                data.append([tweet.full_text, newDate(tweet.created_at)]) 

        elif user == 'simonpeach':
            tweetsPeach = tweepy.Cursor(api.user_timeline, screen_name = user, count = 200, tweet_mode = 'extended').items(limit) 

            for tweet in tweetsPeach:
                data.append([tweet.full_text, newDate(tweet.created_at)])

        elif user == 'ed_aarons':
            tweetsAarons = tweepy.Cursor(api.user_timeline, screen_name = user, count = 200, tweet_mode = 'extended').items(limit)

            for tweet in tweetsAarons:
                data.append([tweet.full_text, newDate(tweet.created_at)])  



        # print(data)
        # df = pd.DataFrame(data, columns = columns)

        return render_template('displayTweets.html', data = data, heading = columns, user = user)

    return render_template('home.html')








if __name__ == "__main__":
    app.run(debug = True)