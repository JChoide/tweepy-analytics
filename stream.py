# author: Jason Chang
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from datetime import datetime
from dateutil import parser
import json
import sys
# import pandas

# authentication keys for Twitter API
consumer_key = 'UTQo43HVZJVmqydZ1S2hiPDaw'
consumer_secret = 'uCXkRQpeJ1Wy55whXsrOFnVuIWBzl3uBmZKtCoGCJyDkbdKkJB'
access_token = '627714227-XgUMt9espQA69FAAw5qbb6KPB0FtqGC2jSt2dyEx'
access_secret = 'FnoJwswLnEFsiY7O3BRqy87ZZMOUdRTmmSja4xTgpTPWX'


class Listener(StreamListener):                                 # edited class based on StreamListener class, determines which tweets to print and in what format
    def on_data(self, data):                                    # defines what to do with incoming data
        d = json.loads(data)                                    # loads tweets in JSON format
        if u'text' in d.keys():                                 # determines if there is text in tweet
            unicode_string = d['text']                          # stores text
            encoded_string = unicode_string.encode('utf-8')     # encodes string using 'utf-8' format
            d['text'] = encoded_string                          # replaces tweet text with the usable format
            game_date = datetime(2015, 7, 24, 0, 0, 0)          # date of the soccer match
            if u'created_at' in d.keys():                       # determines if the date created field is available
                tweet_date = parser.parse(d['created_at'])      # parses date into usable format (datetime)
                tweet_date = datetime(tweet_date.year, tweet_date.month, tweet_date.day)    # stores the datetime format in the default format used
                # for date in pandas.date_range(start_date, periods=86400, freq='S'):       # in case you want to loop through dates
                if tweet_date == game_date:                     # matches tweet date and game date
                    print d                                     # prints tweet if it matches
                else:                                           # else just keep passing to end of script
                    pass
            else:
                pass
        else:
            pass
        return True                                             # continues stream of tweets

    def on_error(self, status):
        print >> sys.stderr, 'Encountered error with status code:', status      # prints out error

    def on_timeout(self):
        print >> sys.stderr, 'Timeout'  # prints out timeout
        return True                     # prevenets killing the stream

if __name__ == '__main__':

    # Puts in Twitter authentication and connects to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitterStream = Stream(auth, Listener())

    # This line filters the stream of tweets by the key words: Benfica and Fiorentina
    twitterStream.filter(track=['fiorentina', 'benfica'])
