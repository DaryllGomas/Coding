import tweepy
import wordcloud
import matplotlib.pyplot as plt
import os
import datetime

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

# Retrieve the most recent tweets from your timeline
tweets = api.user_timeline()

# Create a string of all the tweet texts
tweet_text = ""
for tweet in tweets:
    # Remove any URLs from the tweet text
    text = tweet.text.replace("http", "")
    text = text.replace("t.co", "")
    text = text.replace("sama", "")
    text = text.replace("ahmedsalims", "")
    
    tweet_text += text

# Create a WordCloud object and pass it the text of your tweets
wordcloud = wordcloud.WordCloud().generate(tweet_text)

# Save the word cloud to an image file in the Z:\Python\WordCloud\Image folder
if not os.path.exists("Z:\\Python\\WordCloud\\Image\\"):
    os.makedirs("Z:\\Python\\WordCloud\\Image\\")

# Generate the word cloud image file and save it to the Z:\Python\WordCloud\Image folder
wordcloud.to_file("Z:\\Python\\WordCloud\\Image\\wordcloud.png")

# Format the current date and time to be used as the file name
current_date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Rename the file to the current date and time
os.rename("Z:\\Python\\WordCloud\\Image\\wordcloud.png", "Z:\\Python\\WordCloud\\Image\\wordcloud_{}.png".format(current_date_time))

# Display the word cloud
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
