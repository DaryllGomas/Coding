import tweepy
import wordcloud
import matplotlib.pyplot as plt
import os

# Replace the placeholders with your own API keys 
consumer_key = "-"
consumer_secret = "-"
access_token = "-"
access_token_secret = "-"

# Authenticate the tweepy library with your API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object that you can use to access your Twitter data
api = tweepy.API(auth)

# Retrieve the list of words from the Twitter list you specified
list_id = 1480583392966053888
word_list = api.get_list(list_id)

# Create a string from the list of words
word_string = " ".join(word_list)

# Create a WordCloud object and pass it the string of words
wordcloud = wordcloud.WordCloud().generate(word_string)

# Save the word cloud to an image file in the C:\WordCloud folder
if not os.path.exists("C:\\WordCloud"):
    os.makedirs("C:\\WordCloud")
wordcloud.to_file("C:\\WordCloud\\wordcloud.png")

# Display the word cloud
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
