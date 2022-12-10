import tweepy,re
from wordcloud import WordCloud
from collections import Counter
import os,datetime


#Key and API info
c_k=""
c_s=""
a_t=""
a_t_s=""

a=tweepy.OAuthHandler(c_k,c_s)
a.set_access_token(a_t,a_t_s)

api=tweepy.API(a)

list_id="1480650925869973508"

tweets=tweepy.Cursor(api.list_timeline,list_id=list_id).items()

text=" ".join([tweet.text for tweet in tweets])

text=re.sub(r"[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]*","",text)

word_counts=Counter(text.split())

# Set the frequency of the words you want to exclude to 0
word_counts["and"] = 0
word_counts["the"] = 0
word_counts["to"] = 0
word_counts["of"] = 0
word_counts["t.co"] = 0
word_counts["RT"] = 0
word_counts["is"] = 0
word_counts["on"] = 0
word_counts["in"] = 0
word_counts["a"] = 0
word_counts["i"] = 0
word_counts["you"] = 0
word_counts["for"] = 0
word_counts["are"] = 0
word_counts["that"] = 0
word_counts["from"] = 0
word_counts["with"] = 0
word_counts["have"] = 0
word_counts["this"] = 0
word_counts["be"] = 0
word_counts["the"] = 0
word_counts["I"] = 0
word_counts["it"] = 0
word_counts["The"] = 0
word_counts[""] = 0
word_counts["at"] = 0


wordcloud=WordCloud().generate_from_frequencies(word_counts)

if not os.path.exists("Z:\\Python\\WordCloud\\Image\\"):
    os.makedirs("Z:\\Python\\WordCloud\\Image\\")

wordcloud.to_file("Z:\\Python\\WordCloud\\Image\\wordcloud.png")

current_date_time=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

os.rename("Z:\\Python\\WordCloud\\Image\\wordcloud.png","Z:\\Python\\WordCloud\\Image\\wordcloud_{}.png".format(current_date_time))

import matplotlib.pyplot as plt

plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt.show()