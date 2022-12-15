# Import the necessary modules
import tweepy
from wordcloud import WordCloud
import os

# Authenticate with the Twitter API and access the post's text
# Replace these with your own API keys and tokens
api_key = ""
api_secret_key = ""
access_token = ""
access_token_secret = ""

# Set the URL of the Twitter post and the directory where the file should be saved
post_url = "https://twitter.com/ninaturner/status/1602502497834336257"
directory = "C:\\"

# Use tweepy to authenticate and access the post's text
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get the post's text
post = api.get_status(post_url)
text = post.text

# Generate the word cloud
wordcloud = WordCloud().generate(text)

# Set the file name
file_name = "wordcloud.png"

# Use the os.path.join() method to combine the directory and file name into a full path
file_path = os.path.join(directory, file_name)

# Save the file to the specified path
wordcloud.to_file(file_path)








