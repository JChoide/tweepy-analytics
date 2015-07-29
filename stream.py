from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from datetime import datetime
# import pandas
import json
import sys
from dateutil import parser

consumer_key = 'UTQo43HVZJVmqydZ1S2hiPDaw'
consumer_secret = 'uCXkRQpeJ1Wy55whXsrOFnVuIWBzl3uBmZKtCoGCJyDkbdKkJB'
access_token = '627714227-XgUMt9espQA69FAAw5qbb6KPB0FtqGC2jSt2dyEx'
access_secret = 'FnoJwswLnEFsiY7O3BRqy87ZZMOUdRTmmSja4xTgpTPWX'


class Listener(StreamListener):
    def on_data(self, data):
        d = json.loads(data)
        if u'text' in d.keys():
            unicode_string = d['text']
            encoded_string = unicode_string.encode('utf-8')
            d['text'] = encoded_string
            # print d['text']
            game_date = datetime(2015, 7, 24, 0, 0, 0)
            if u'created_at' in d.keys():
                tweet_date = parser.parse(d['created_at'])
                tweet_date = datetime(tweet_date.year, tweet_date.month, tweet_date.day)
                # for date in pandas.date_range(start_date, periods=86400, freq='S'):
                if tweet_date == game_date:
                    print d['created_at'], "\t", d['text']
                else:
                    pass
            else:
                pass
        else:
            pass
        return True

    def on_error(self, status):
        # print status
        print >> sys.stderr, 'Encountered error with status code:', status      # prints out error

    def on_timeout(self):
        print >> sys.stderr, 'Timeout'  # prints out timeout
        return True  # Don't kill the stream

if __name__ == '__main__':

    # Puts in Twitter authentication and connects to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitterStream = Stream(auth, Listener())

    # This line filters Twitter Streams to capture data by the keywords:
    # twitterStream.filter(track=['python', 'javascript', 'ruby'])
    twitterStream.filter(track=['fiorentina', 'benfica'])
