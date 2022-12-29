import tweepy, re, time
from wordcloud import WordCloud
from collections import Counter
import os, datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import cv2

# Set your Twitter API keys and access tokens here
c_k = "O5SYqBKzNdwHZGYG3xlkTmefx"
c_s = "Qm1hqZ1USp5atdDHSq2L4u2om7k9lSZ4hpKBX2R5qigvqtpIbK"
a_t = "14149962-IUJxoENFZ30uhl3I94HAYUhlHkrWn1chONZpmdnNB"
a_t_s = "JR5KaIahaY7lvjm9Fg7HxH7K6lezXvQCQnSWLJMr7TsWe"

a = tweepy.OAuthHandler(c_k, c_s)
a.set_access_token(a_t, a_t_s)

api = tweepy.API(a)

# Create a function that will be called when the user clicks the "Focused" button
def run_task(run):
    # If the user clicked the "Focused" button, run the task
    if run:
       
        # Set the list IDs here
        list_ids = ["1480583392966053888", "1481074628867194880", "1481565861479231488"]

        # Initialize a list to store the data for each list
        list_data = []

        # Iterate over the list IDs
        for list_id in list_ids:
            # Use the "since_id" parameter to only download tweets from the last 6 hours
            tweets = tweepy.Cursor(api.list_timeline, list_id=list_id, since_id=str(int(time.time() - 6*60*60))).items()

            # Join all of the tweets into a single string
            text = " ".join([tweet.text for tweet in tweets])

            # Remove mentions of other Twitter users from the text
            text = re.sub(r"[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]*", "", text)

            # Count the frequency of each word
            word_counts = Counter(text.split())

            # Set the frequency of common words to 0 to exclude them from the word cloud
            common_words = ["[DB]", "They", "they", "You", "It", "In", ",", ".", "like", "&amp;", "_inc","back", "And", "has", "our", "up", "one", "would", "want", "been", "not", "inc", "out", "can", "what", "but", "more", "_", "_xyz", "_szilagyi", "and", "the", "to", "of", "t.co", "RT", "is",
            "on", "in", "a", "i", "you", "for", "are", "that", "from", "with", "have", "this", "be", "the", "I", "it", "The", "_vanepps", "at", "your", "will", "was", "my", "about", "as", "so", "all", "by", "an", "just", "if", "me", "we", "This", "then", "or", "If"]

            # Iterate over the common words and set their frequency to 0 in the word_counts dictionary
            for word in common_words:
                word_counts[word] = 0

            # Generate the word cloud
            wordcloud = WordCloud().generate_from_frequencies(word_counts)

            # Store the word cloud data in the list
            list_data.append(wordcloud.to_array())

        # Create a video capture object
        cap = cv2.VideoCapture(0)

        # Set the width and height of the video capture object
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Create a video writer object to save the video
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter('live_video.avi', fourcc, 20.0, (width, height))

        # Set the font and color for the text
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 255, 255)
        font_scale = 1
        thickness = 2

        # Set the length of the fade transition between lists
        fade_length = 25

        # Set the length of time each list is displayed
        display_length = 50

        # Set the start and end points for the alpha channel
        alpha_start = 0
        alpha_end = 255

        # Set the counter to 0
        counter = 0

        # Loop until the user clicks the "Stop" button
        while run:
            # Get the current frame
            ret, frame = cap.read()

            # Get the current list data
            data = list_data[counter % len(list_data)]

            # Calculate the alpha value for the current frame
            alpha = int((alpha_end - alpha_start) * (counter % (fade_length + display_length)) / fade_length) + alpha_start

            # Create a copy of the current frame with an alpha channel
            frame_alpha = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

            # Create an alpha mask for the list data
            alpha_mask = cv2.merge((data, data, data, data * alpha / 255))

            # Overlay the list data on top of the current frame
            cv2.addWeighted(alpha_mask, 1, frame_alpha, 1, 0, frame_alpha)

            # Write the current frame to the video file
            out.write(frame_alpha)

            #Display the current frame
            cv2.imshow('Live Video', frame_alpha)
                       
            # Get the size of the text
            text_size = cv2.getTextSize(list_ids[counter % len(list_data)], font, font_scale, thickness)[0]

            # Calculate the coordinates for the text
            text_x = (width - text_size[0]) // 2
            text_y = (height - text_size[1]) // 2

            # Add the text to the frame
            cv2.putText(frame_alpha, list_ids[counter % len(list_data)], (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)

            # Increment the counter
            counter += 1

            # Check if the user clicked the "Stop" button
            if not run:
                break

            # Wait for the specified amount of time
            time.sleep(0.05)

        # Release the video capture and video writer objects
        cap.release()
        out.release()

        # Close all windows
        cv2.destroyAllWindows()

# Create the GUI
root = tk.Tk()
root.title("Twitter Word Cloud")

# Create the "Start" and "Stop" buttons
start_button = tk.Button(root, text="Start", command=lambda: run_task(True))
stop_button = tk.Button(root, text="Stop", command=lambda: run_task(False))

# Place the buttons in the GUI
start_button.pack()
stop_button.pack()

# Run the GUI loop
root.mainloop()
