import os
import youtube_dl

# Set the file path to the playlists.txt file
file_path = "c:\\users\iccanui\desktop\playlists.txt"

# Open the file in read mode
with open(file_path, "r", encoding='utf-8') as file:
    # Read the contents of the file and split it into a list of strings
    playlists = file.read().splitlines()

# Define the options for the download
options = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:\\Audio\\%(playlist)s\\%(title)s.%(ext)s',
    'audio-format': 'mp3',
    'audio-quality': '192'
}

# Iterate over the playlists
for i, playlist in enumerate(playlists):
    if i % 2 == 0: #even number
        current_playlist = playlist
        if not current_playlist.startswith("-"):
            options['outtmpl'] = options['outtmpl'].replace("%(playlist)s", current_playlist)
            # Create the directory if it doesn't exist
            os.makedirs(f"C:\\Audio\\{current_playlist}", exist_ok=True)
    else:
        # Make the search on youtube
        query = f"{playlist} {current_playlist} audio"
        url = f"ytsearch1:{query}"
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([url])
