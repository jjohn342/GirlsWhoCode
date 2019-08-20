'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
filtered_words = ["of", "in", "the", "for", "they", "if", "with", "is", "https"]

polarity = []
subjectivity = []
i = 0
bigtweet = ""
for tweet in tweetData:
    blob = TextBlob(tweet["text"])
    tweet_p = blob.polarity
    tweet_s = blob.subjectivity
    polarity.append(tweet_p)
    subjectivity.append(tweet_s)
    i += 1
    #bigtweet += text
#blog = TextBlob(tweet)
filtered = {}

#wordslist = bigblob.words
for word in filtered_words:
    #filters here
    if len(word) < 2:
        continue
    if not word.isalpha():
        continue
    if word.lower() in filtered_words:
        continue
    filtered[word.lower()] = blob.word_counts[word.lower()]

print(word)

final1 = sum(polarity)
len1 = len(polarity)
avg_p = final1 / len1

final2 = sum(subjectivity)
len2 = len(subjectivity)
avg_s = final2 / len2

print(avg_p)
print(avg_s)


# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)

plt.title('Pol Histogram')
plt.xlabel('Polarity')
plt.ylabel('Rate')
plt.grid(True)
plt.hist(polarity , bins = 5)
plt.axis([-1.00, 1.00, 0, 60])
plt.show()

plt.title('Sub Histogram')
plt.xlabel('Subjectivity')
plt.ylabel('Rate')
plt.grid(True)
plt.hist(subjectivity, bins = 5)
plt.axis([-1.00, 1.00, 0, 60])
plt.show()

plt.scatter(polarity, subjectivity)
plt.show()

all_tweets = ', '.join(tweet['text'] for tweet in tweetData)
tb = TextBlob(all_tweets)
#filtered_words = []
print(all_tweets)

print(str(tweet))

wordcloud = WordCloud().generate(all_tweets)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
#generate_from_text(text)
