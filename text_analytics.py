# author: jason chang
import json
import matplotlib.pyplot as plt
from pandas import *
# from prettytable import *       # if prettier tables are needed
# import numpy as np              # if arithmetic needs to be done

plt.close('all')    # closes all plots
tweets_data_path = 'C:\Users\Jason Chang\Dropbox\Projects\Twitter API\soccer.txt'   # location of output file

# loads all of the tweets into a list
tweets_data = []                                    # creates empty list for tweets to be loaded into
tweets_file = open(tweets_data_path, "r")           # opens tweet text file
for line in tweets_file:                            # loads tweets into list
    try:
        tweet = json.loads(line)                    # loads tweet into json/dictionary
        tweets_data.append(tweet)                   # appends tweet to list
    except:
        continue                                    # continue on to next iteration
print "Number of Tweets:", len(tweets_data)         # prints number of tweets
print "\n"

# loads all the tweets into a pandas data frame for easier manipulation
tweets = DataFrame()                                                    # creates tweet data frame
tweets['Text'] = map(lambda tweet: tweet['text'], tweets_data)          # tweet text column
tweets['Language'] = map(lambda tweet: tweet['lang'], tweets_data)      # tweet language column
tweets['Country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)   # tweet country column (returns none, if not available)

tweets_by_country = tweets['Country'].value_counts()                # determines most frequent tweet countries
print tweets_by_country                                             # prints out countries and how many tweets came from each in descending order
# f, ax = plt.subplots()                                            # uncomment to have separate country plot
# ax.set_xlabel("Country")
# ax.set_ylabel("Number of Tweets")
# ax.set_title("Top 5 Countries")
# tweets_by_country[:5].plot(ax=ax, kind='bar', color='green')
# plt.xticks(rotation=0)
print "\n"  # prints new space

# x = np.linspace(0, 2 * np.pi, 400)        # if messing with graphs and need a simple plot to chart with
# y = np.sin(x ** 2)

languages = ['Portuguese', 'Turkish', 'English', 'Italian', 'French', 'Spanish']   # top 6 languages
tweets_by_lang = tweets['Language'].value_counts()         # returns object containing counts of unique values in descending order
print tweets_by_lang                                       # prints out most common languages
print "\n"                                                 # prints out new line

# produces both plots: bar graph of most frequent languages and bar graph of most frequent countries
f, ax = plt.subplots(2)                                    # creates plot
ax[1].tick_params(axis='x', labelsize=12)                  # changes x tick font size
ax[1].tick_params(axis='y', labelsize=12)                  # changes y tick font size
ax[1].set_xlabel('Languages', fontsize=12)                 # x axis label
ax[1].set_ylabel('Number of tweets', fontsize=12)          # y axis label
ax[1].set_title('Top 6 Languages', fontsize=15, fontweight='bold')      # graph title
ax[0].tick_params(axis='x', labelsize=9)                                # edits x tick labels
ax[0].tick_params(axis='y', labelsize=12)                               # edits y tick label
ax[0].set_xlabel("Country", fontsize=12)                                # edits x label
ax[0].set_ylabel("Number of Tweets", fontsize=12)                       # edits y label
ax[0].set_title("Top 5 Countries", fontsize=15, fontweight='bold')      # set title
tweets_by_lang[:6].plot(ax=ax[1], kind='bar', color='red')              # fills in plot with axis settings and data (top 6)
ax[1].set_xticklabels(languages)                                        # sets names of x tick labels
tweets_by_country[:5].plot(ax=ax[0], kind='bar', color='green')         # bar plot of top 5 frequency countries
plt.xticks(rotation=0)                                                  # sets x tick labels to horizontal
f.subplots_adjust(hspace=1)                                             # sets space between graphs

# function to find if a word is in the text of a tweet
def word_in_text(word, text):             # determines if word is in tweet
    word = word.lower()                   # converts word to lowercase
    text = text.lower()                   # converts full tweet to lowercase
    matches = re.search(word, text)       # searches for word in tweet
    if matches:                           # if it matches, print true, else print false
        return True
    else:
        return False

# adds Fiorentina and Benfica columns
tweets['Fiorentina'] = tweets['Text'].apply(lambda tweet: word_in_text('fiorentina', tweet))    # applies word_in_text formatting to all tweets containing fiorentina
tweets['Benfica'] = tweets['Text'].apply(lambda tweet: word_in_text('benfica', tweet))          # applies word_in_text formatting to all tweets containing benfica

# number of tweets per team
print "Fiorentina:", tweets['Fiorentina'].value_counts()[True]     # number of fiorentina tweets
print "Benfica:", tweets['Benfica'].value_counts()[True]           # number of benfica tweets

# x and y values
teams = ['Fiorentina', 'Benfica']   # team names
tweets_by_team = [tweets['Fiorentina'].value_counts()[True], tweets['Benfica'].value_counts()[True]]    # counts number of True's in Fiorentina column and in Benfica column and stores it into a list

# bar plot of tweets per team
x_pos = list(range(len(teams)))                                        # [0, 1]
width = 0.9                                                            # 1 = no space between bars
fig, ax = plt.subplots()                                               # subplot(row, col, subplot chosen to edit)
plt.bar(x_pos, tweets_by_team, width, alpha=0.5, color='purple')       # make bar plot (x, y, width, opacity, color
# Setting axis labels and ticks
ax.set_xlabel('Teams', fontsize=13)                       # y axis label
ax.set_ylabel('Number of tweets', fontsize=13)                       # y axis label
ax.set_title('Ranking: Fiorentina vs. Benfica (Raw data)', fontsize=15, fontweight='bold')      # title of chart
ax.set_xticks([p + 0.5 * width for p in x_pos])     # x tick separation
ax.set_xticklabels(teams)                           # x tick labels
plt.grid()                                          # turns axes grid on

# shows/outputs all plots
plt.show()
