import tweepy
import wordcloud
import matplotlib.pyplot as plt
import os
import smtplib

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
    tweet_text += tweet.text

# Create a WordCloud object and pass it the text of your tweets
wordcloud = wordcloud.WordCloud().generate(tweet_text)

# Save the word cloud to an image file in the C:\WordCloud folder
if not os.path.exists("C:\\WordCloud"):
    os.makedirs("C:\\WordCloud")
wordcloud.to_file("C:\\WordCloud\\wordcloud.png")

# Display the word cloud
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# The following code will email the image file to a gmail account

# Replace the placeholders with the email address and password of the Gmail account you want to use
gmail_user = "-"
gmail_password = "-"

# Create an SMTP object that you can use to send the email
smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.starttls()

# Login to the Gmail account
smtp_obj.login(gmail_user, gmail_password)

# Compose the email
from_address = gmail_user
to_address = gmail_user
subject = "Twitter word cloud"
body = "Here is the word cloud of your recent tweets."
email_text = f"Subject: {subject}\n\n{body}"

# Attach the image of the word cloud to the email
file_path = "C:\\WordCloud\\wordcloud.png"
with open(file_path, "rb") as img:
    file_data = img.read()
    file_name = os.path.basename(file_path)
    mime_type = "image/png"  # This is the MIME type for a PNG image

# Create the attachment tuple with the file name, data, and MIME type
attachment = (file_name, file_data, mime_type)


# Send the email
smtp_obj.sendmail(from_address, to_address, email_text.encode("utf-8"), [attachment])

# Log out of the Gmail account
smtp_obj.quit()
