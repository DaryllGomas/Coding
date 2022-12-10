import tweepy, re, time
from wordcloud import WordCloud
from collections import Counter
import os, datetime

# Set your Twitter API keys and access tokens here
c_k = "-"
c_s = "-"
a_t = "-"
a_t_s = "-"

a = tweepy.OAuthHandler(c_k, c_s)
a.set_access_token(a_t, a_t_s)

api = tweepy.API(a)

# Set the list ID here
list_id = "1480650925869973508"

# Use the "since_id" parameter to only download tweets from the last 4 hours
tweets = tweepy.Cursor(api.list_timeline, list_id=list_id, since_id=str(int(time.time() - 4*60*60))).items()

# Join all of the tweets into a single string
text = " ".join([tweet.text for tweet in tweets])

# Remove mentions of other Twitter users from the text
text = re.sub(r"[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]*", "", text)

# Count the frequency of each word
word_counts = Counter(text.split())

# Set the frequency of common words to 0 to exclude them from the word cloud
common_words = ["_", "_xyz", "_szilagyi", "and", "the", "to", "of", "t.co", "RT", "is", "on", "in", "a", "i", "you", "for", "are", "that", "from", "with", "have", "this", "be", "the", "I", "it", "The", "_vanepps", "at"]
for word in common_words:
    word_counts[word] = 0

# Generate the word cloud
wordcloud = WordCloud().generate_from_frequencies(word_counts)

# Save the word cloud to a file
if not os.path.exists("Z:\\Python\\WordCloud\\Image\\"):
    os.makedirs("Z:\\Python\\WordCloud\\Image\\")

wordcloud.to_file("Z:\\Python\\WordCloud\\Image\\wordcloud.png")

# Rename the file with the current date and time
current_date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
os.rename("Z:\\Python\\WordCloud\\Image\\wordcloud.png", "Z:\\Python\\WordCloud\\Image\\Focused_{}.png".format(current_date_time))

# Display the word cloud
import matplotlib.pyplot as plt

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

# Add the file name to the bottom of the image
plt.text(0.5, -0.2, "Focused_{}.png".format(current_date_time), horizontalalignment="center")

plt.show()
