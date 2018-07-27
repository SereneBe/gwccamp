'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''
###############################################
####PT:1 ANALYZE THE FEELINGS IN THE TWEETS####
###############################################

#Import your Twitter data, json library, and textblob library.
import json
from textblob import TextBlob
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Create a list for polarity and subjectivity.
pol = []
sub = []

#For each tweet, make a textblob from the text.
for tweet in tweetData:
    tb = TextBlob(tweet["text"])
    #Store each tweet's polarity and subjectivity in the list.
    pol.append(tb.polarity)
    sub.append(tb.subjectivity)

#Print out the average polarity and subjectivity.
avgPol = sum(pol)/len(pol)
print(avgPol)

avgSub = sum(sub)/len(sub)
print(avgSub)

###################################
####PT:2 VISUALIZE THE FEELINGS####
###################################

#Create a histogram plot in matplotlib.
import matplotlib.pyplot as plt

    #Give it polarity data and a list of bins.
plt.hist(pol, bins=[-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])

#Set the x and y labels.
plt.xlabel("Polarity")
plt.ylabel("Number of Tweets")

plt.title("Histogram of Tweet Polarity")

#Set the axis to fit your data range.
plt.axis([-1.1, 1.1, 0, len(pol)])
#Show your plot.
plt.show()

#Create another histogram for subjectivity.
plt.hist(sub, bins=[0, 0.25, 0.5, 0.75, 1])

plt.xlabel("Subjectivity")
plt.ylabel("Number of Tweets")

plt.title("Histogram of Tweet Subjectivity")

plt.axis([-1.1, 1.1, 0, len(sub)])

plt.show()

####################################
####PT: 3 VISUALIZE THE LANGUAGE####
####################################


#Add `from wordcloud import WordCloud` to the beginning of your file
from wordcloud import WordCloud

#Combine all the tweets into one large string.
    #Remember loops and string operators?
bigstring = ""
for tweet in tweetData:
    bigstring = bigstring + " " + tweet["text"]

#Create a textblob from the combined string.
    tb = TextBlob(bigstring)

#Generate your own dictionary of `filteredWords[word] = count` by looping TextBlob's words list and word_counts dictionary.
words={}
for word in tb.words:
    words[word] = tb.words.count(word)
print(words)

    #Skip words you don't want in your filtered dictionary.
        #Try filtering words that are less than three letters.
        #Try creating a list of common words to filter like "and," "about," "the," "http," etc. and skip words `in` that list.
        #Try filtering things that aren't words.
filteredwords = {}
filter = ["your", "https", "will", "about", "wish", "this", "they", "that", "the", "and", "http", "a", "i", "at", "we", "in", "on", ]

for word in tb.words:
    word = word.lower()
    if word.isalpha():
        if word not in filter and len(word)>3:
            filteredwords[word] = tb.words.count(word)
print(filteredwords)

#Generate a word cloud from the frequencies.
cloud = WordCloud(background_color = 'white',max_font_size = 50).generate_from_frequencies(filteredwords)
plt.figure()
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
