from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
import json

consumer_key = 'UTQo43HVZJVmqydZ1S2hiPDaw'
consumer_secret = 'uCXkRQpeJ1Wy55whXsrOFnVuIWBzl3uBmZKtCoGCJyDkbdKkJB'
access_token = '627714227-XgUMt9espQA69FAAw5qbb6KPB0FtqGC2jSt2dyEx'
access_secret = 'FnoJwswLnEFsiY7O3BRqy87ZZMOUdRTmmSja4xTgpTPWX'


# class Listener(StreamListener):
#     def on_data(self, data):
#         d = json.loads(data)
#         print d['id'], "\t", d['created_at'],"\t", d['text']
#         return True
#
#     def on_error(self, status):
#         print(status)

if __name__ == '__main__':

    # Puts in Twitter authentication and connects to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # twitterStream = Stream(auth, Listener())
    # twitterStream.filter(track=["a"])
    api = API(auth)
    start_id = 624368394029125633
    end_id = 624730781902999552
    counter = end_id
    while counter >= start_id:
        results = api.search(q="fiorentina", since_id=counter, max_id=counter, count=1)
        for result in results:
            unicode_string = result.text
            encoded_string = unicode_string.encode('utf-8')
            print encoded_string
            print result.created_at
        counter -= 1
