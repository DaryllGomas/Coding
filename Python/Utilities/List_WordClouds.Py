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

# Define a function to run the task for a specific list
def run_task(list_id, list_name):
    # Use the "since_id" parameter to only download tweets from the last 6 hours
    tweets = tweepy.Cursor(api.list_timeline, list_id=list_id, since_id=str(int(time.time() - 6*60*60))).items()

    # Join all of the tweets into a single string
    text = " ".join([tweet.text for tweet in tweets])

    # Remove mentions of other Twitter users from the text
    text = re.sub(r"[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]*", "", text)

    # Count the frequency of each word
    word_counts = Counter(text.split())

    # Set the frequency of common words to 0 to exclude them from the word cloud
    common_words = ["[DB]", "They", "they", "You", "It", "In", ",", ".", "like", "&amp;", "_inc","back", "And", "has", "our", "up", "one", "would", "want", "been", "not", "inc", "out", "can", "what", "but", "more", "_", "_xyz", "_szilagyi", "and", "the", "to", "of", "t.co", "RT", "is", "on", "in", "a", "i", "you", "for", "are", "that", "from", "with", "have", "this", "be", "the", "I", "it", "The", "_vanepps", "at", "your", "will", "was", "my", "about", "as", "so", "all", "by", "an", "just", "if", "me", "we", "This", "then", "or", "If"]

    # Iterate over the common words and set their frequency to 0 in the word_counts dictionary
    for word in common_words:
        word_counts[word] = 0

    # Generate the word cloud
    wordcloud = WordCloud().generate_from_frequencies(word_counts)

    # Save the word cloud to a file
    if not os.path.exists(f"C:\\Python\\WordCloud\\Image\\{list_name}\\"):
        os.makedirs(f"C:\\Python\\WordCloud\\Image\\{list_name}\\")

    wordcloud.to_file(f"C:\\Python\\WordCloud\\Image\\{list_name}\\wordcloud.png")

    # Rename the file with the current date and time
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.rename(f"C:\\Python\\WordCloud\\Image\\{list_name}\\wordcloud.png", f"C:\\Python\\WordCloud\\Image\\{list_name}\\wordcloud_{current_date_time}.png")

# Define the lists to run the task on
list_name = [
    {"id": "1361242639111135234", "name": "Focused"},
    {"id": "1430346349375938572", "name": "Crypto"},
    {"id": "1366729121678589959", "name": "Macro"},
    {"id": "1579939259070709760", "name": "AI"},
]

# Iterate over the lists and run the task for each one
for l in list_name:
    run_task(l["id"], l["name"])

# Your Twitter API keys
consumer_key = 'LwiJhxcRP7rw3QuVoDxyDwEpa'
consumer_secret = 'MVMPTIPqJnF8NeK1g07Aohkfe0XVJbLI3MBjDNjAZ7QFZAZnHT'
access_token = '1296735650717167616-JeXIFW5hb9evw9oyVz2UU7MxorQT98'
access_token_secret = '6ZDVhlHvZHJR8t84aPDMGEu6QAh4l6GGedLnBI7lebh8P'

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Scan the folder for the latest Focused image
folder = ("C:\\Python\\WordCloud\\Image\\Focused\\")
latest_image = max(os.listdir(folder), key=lambda x: os.stat(os.path.join(folder, x)).st_mtime)
image_path = os.path.join(folder, latest_image)

# Upload the image to Twitter
media = api.media_upload(image_path)
api.update_status(status='Focused list WordCloud of the Day \n \nThe best posters from my curated lists', media_ids=[media.media_id])



## Scan the folder for the latest Crypto image
folder = ("C:\\Python\\WordCloud\\Image\\Crypto\\")
latest_image = max(os.listdir(folder), key=lambda x: os.stat(os.path.join(folder, x)).st_mtime)
image_path = os.path.join(folder, latest_image)

## Upload the image to Twitter
media = api.media_upload(image_path)
api.update_status(status='Crypto list WordCloud of the Day \n \nFor all your #Blockchain and #Crypto needs! \n Main focus is Blue chips like #BTC #ETH #Solana , etc', media_ids=[media.media_id])



### Scan the folder for the latest Macro image
folder = ("C:\\Python\\WordCloud\\Image\\Macro\\")
latest_image = max(os.listdir(folder), key=lambda x: os.stat(os.path.join(folder, x)).st_mtime)
image_path = os.path.join(folder, latest_image)

### Upload the image to Twitter
media = api.media_upload(image_path)
api.update_status(status='Macro list WordCloud of the Day \n \nFor all your #fintwit , $SPY and $QQQ needs!', media_ids=[media.media_id])



#### Scan the folder for the latest AI image
folder = ("C:\\Python\\WordCloud\\Image\\AI\\")
latest_image = max(os.listdir(folder), key=lambda x: os.stat(os.path.join(folder, x)).st_mtime)
image_path = os.path.join(folder, latest_image)

#### Upload the image to Twitter
media = api.media_upload(image_path)
api.update_status(status='AI list WordCloud of the Day \n \nFor all your #ArtificialIntelligence needs !', media_ids=[media.media_id])
