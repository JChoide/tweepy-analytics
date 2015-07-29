# author: jason chang
from tweepy import OAuthHandler
from tweepy import API

consumer_key = 'UTQo43HVZJVmqydZ1S2hiPDaw'
consumer_secret = 'uCXkRQpeJ1Wy55whXsrOFnVuIWBzl3uBmZKtCoGCJyDkbdKkJB'
access_token = '627714227-XgUMt9espQA69FAAw5qbb6KPB0FtqGC2jSt2dyEx'
access_secret = 'FnoJwswLnEFsiY7O3BRqy87ZZMOUdRTmmSja4xTgpTPWX'

if __name__ == '__main__':

    # Puts in Twitter authentication and connects to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = API(auth)
    
    # Used to output all tweets within a given date range with specified key words
    start_id = 624368394029125633           # id of the tweet with the starting time 
    end_id = 624730781902999552             # id of the tweet with the ending time
    while(end_id >= start_id)               # makes sure end_id is greater than or equal to the start_id number, to keep it within date range
        id_numbers = []                     # creates an empty list for the id numbers that will be loaded in by the for loop
        results = api.search(q="fiorentina", since_id=start_id, max_id=end_id, count=200)   # list of 200 or less most recent tweets between the ids that have the key word fiorentina in it
        for result in results:              # for each tweet do this:
            unicode_string = result.text    # stores text in var
            encoded_string = unicode_string.encode('utf-8')     # converts text to string using 'utf-8'
            result.text = encoded_string                        # reassigns text to the converted string
            print result                                        # prints out formatted string
            id_numbers.append(result.id)                        # appends id of tweet to end of id list
        end_id = min(id_number)                                 # end_id is reassigned to the minimum id number in the list of id numbers
