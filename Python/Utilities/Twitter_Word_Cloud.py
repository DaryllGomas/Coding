import tweepy

# Replace the placeholders with your own API keys ( these keys are depreciated)
consumer_key = "input key"
consumer_secret = "input secret"
access_token = "input token"
access_token_secret = "input secret"

# Authenticate the tweepy library with your API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object that you can use to access your Twitter data
api = tweepy.API(auth)
# Retrieve the most recent tweets from your timeline
tweets = api.user_timeline()

# Print the text of each tweet
for tweet in tweets:
    print(tweet.text)
    
from wordcloud import WordCloud

# Create a WordCloud object and pass it the text of your tweets
wordcloud = WordCloud().generate(tweet_text)

# Save the word cloud to an image file
wordcloud.to_file("wordcloud.png")

import matplotlib.pyplot as plt

# Display the word cloud
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
