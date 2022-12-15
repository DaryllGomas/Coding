import tweepy, re, time
from wordcloud import WordCloud
from collections import Counter
import os, datetime
import tkinter as tk

# Set your Twitter API keys and access tokens here
c_k = ""
c_s = ""
a_t = ""
a_t_s = ""

a = tweepy.OAuthHandler(c_k, c_s)
a.set_access_token(a_t, a_t_s)

api = tweepy.API(a)

# Create a function that will be called when the user clicks the "Focused" button
def run_task(run):
    # If the user clicked the "Yes" button, run the task
    if run:
       
        # Set the list ID here
        list_id = "1480583392966053888"

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
        plt.text(0.5, -0.2, "Focused_{}.png".format(current_date_time), horizontalalignment="left")

        plt.show()

## If the user clicked the "Crypto" button, destroy the window
def run_task2(run):
        if run:

        # Set the list ID here
            list_id = "1480650925869973508"

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
        if not os.path.exists("Z:\\Python\\WordCloud\\Image\\"):
            os.makedirs("Z:\\Python\\WordCloud\\Image\\")

        wordcloud.to_file("Z:\\Python\\WordCloud\\Image\\wordcloud.png")

        # Rename the file with the current date and time
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        os.rename("Z:\\Python\\WordCloud\\Image\\wordcloud.png", "Z:\\Python\\WordCloud\\Image\\Crypto_{}.png".format(current_date_time))

        # Display the word cloud
        import matplotlib.pyplot as plt

        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")

        # Add the file name to the bottom of the image
        plt.text(0.5, -0.2, "Crypto_{}.png".format(current_date_time), horizontalalignment="left")

        plt.show()

### If the user clicked the "Exit" button, destroy the window
def run_task_end(run):
        if run:
        #Close task window
            root.destroy()
        

# Create a window
root = tk.Tk()
root.geometry("200x100")

# Get the screen's width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position of the window
x_coord = (screen_width/2) - (200/2)
y_coord = (screen_height/2) - (100/2)

# Set the window's position and size
root.geometry("200x100+%d+%d" % (x_coord, y_coord))

# Add a label asking the user if they want to run the task
label = tk.Label(root, text=" Initiate Which list for scan? ")
label.pack()

# Add a "Focused" button that will call the "run_task" function with the "True" argument when clicked
yes_button = tk.Button(root, text="Focused", command=lambda: run_task(True))
yes_button.pack()

# Add a "Crypto" button that will call the "run_task" function with the "True" argument when clicked
no_button = tk.Button(root, text="Crypto", command=lambda: run_task2(True))
no_button.pack()

# Add a "Exit" button that will call the "run_task_exit" function with the "True" argument when clicked
no_button = tk.Button(root, text="Exit", command=lambda: run_task_end(True))
no_button.pack()

# Start the event loop
root.mainloop()



