import tweepy, re, time
from wordcloud import WordCloud
from collections import Counter
import os, datetime
import tkinter as tk

# Set your Twitter API keys and access tokens here
c_k = "-"
c_s = "-"
a_t = "-"
a_t_s = "-"

a = tweepy.OAuthHandler(c_k, c_s)
a.set_access_token(a_t, a_t_s)

api = tweepy.API(a)

# Create a function that will be called when the user clicks the "Yes" or "No" button
def run_task(run):
    # If the user clicked the "Yes" button, run the task
    if run:
        # Set the list ID here
        list_id = "-"

        # Use the "since_id" parameter to only download tweets from the last 6 hours
        tweets = tweepy.Cursor(api.list_timeline, list_id=list_id, since_id=str(int(time.time() - 6*60*60))).items()

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
        
        #Close task window
        root.destroy()

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

# If the user clicked the "No" button, destroy the window
    else:
        root.destroy()

# Create a window
root = tk.Tk()
root.geometry("200x100")

# Add a label asking the user if they want to run the task
label = tk.Label(root, text="Do you want to run the task?")
label.pack()

# Add a "Yes" button that will call the "run_task" function with the "True" argument when clicked
yes_button = tk.Button(root, text="Yes", command=lambda: run_task(True))
yes_button.pack()

# Add a "No" button that will call the "run_task" function with the "False" argument when clicked
no_button = tk.Button(root, text="No", command=lambda: run_task(False))
no_button.pack()

# Start the event loop
root.mainloop()

