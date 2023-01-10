import tweepy
import os

# Your Twitter API keys
consumer_key = '-'
consumer_secret = '-'
access_token = '-'
access_token_secret = '-'

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Scan the folder for the latest Focused image
folder = ("Z:\\Python\\WordCloud\\Image\\Focused\\")
latest_image = max(os.listdir(folder), key=lambda x: os.stat(os.path.join(folder, x)).st_mtime)
image_path = os.path.join(folder, latest_image)

# Upload the image to Twitter
media = api.media_upload(image_path)
api.update_status(status='Focused list WordCloud of the Day \n \nThe best posters from my curated lists', media_ids=[media.media_id])



## Scan the folder for the latest Crypto image
folder = ("Z:\\Python\\WordCloud\\Image\\Crypto\\")
latest_image = max(os.listdir(folder), key=lambda x: os.stat(os.path.join(folder, x)).st_mtime)
image_path = os.path.join(folder, latest_image)

## Upload the image to Twitter
media = api.media_upload(image_path)
api.update_status(status='Crypto list WordCloud of the Day \n \nFor all your #Blockchain and #Crypto needs! \n Main focus is Blue chips like #BTC #ETC #Solana , etc', media_ids=[media.media_id])



### Scan the folder for the latest Macro image
folder = ("Z:\\Python\\WordCloud\\Image\\Macro\\")
latest_image = max(os.listdir(folder), key=lambda x: os.stat(os.path.join(folder, x)).st_mtime)
image_path = os.path.join(folder, latest_image)

### Upload the image to Twitter
media = api.media_upload(image_path)
api.update_status(status='Macro list WordCloud of the Day \n \nFor all your #fintwit , $SPY and $QQQ needs!', media_ids=[media.media_id])



#### Scan the folder for the latest AI image
folder = ("Z:\\Python\\WordCloud\\Image\\AI\\")
latest_image = max(os.listdir(folder), key=lambda x: os.stat(os.path.join(folder, x)).st_mtime)
image_path = os.path.join(folder, latest_image)

#### Upload the image to Twitter
media = api.media_upload(image_path)
api.update_status(status='AI list WordCloud of the Day \n \nFor all your #ArtificialIntelligence needs !', media_ids=[media.media_id])