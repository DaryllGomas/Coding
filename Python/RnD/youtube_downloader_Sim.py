import os
import youtube_dl
import time

# Set the file path to the playlists.txt file
file_path = "z:\\Audio\playlists.txt"

# Open the file in read mode
with open(file_path, "r", encoding='utf-8') as file:
    # Read the contents of the file and split it into a list of strings
    playlists = file.read().splitlines()

# Define the options for the download
options = {
    'format': 'bestaudio/best',
    'outtmpl': 'Z:\\Audio\\%(playlist)s\\%(title)s.%(ext)s',
    'audio-format': 'mp3',
    'audio-quality': '192',
}

# Create a variable to track the number of 403 errors encountered
errors = 0

# Iterate over the playlists
for i, playlist in enumerate(playlists):
    if i % 2 == 0: #even number
        if not playlist.startswith("-"):
            current_playlist = playlist
            options['outtmpl'] = options['outtmpl'].replace("%(playlist)s", current_playlist)
            # Create the directory if it doesn't exist
            os.makedirs(f"Z:\\Audio\\{current_playlist}", exist_ok=True)
    else:
        # Make the search on youtube
        query = f"{playlist} {current_playlist} audio"
        url = f"ytsearch1:{query}"
        while True:
            try:
                with youtube_dl.YoutubeDL(options) as ydl:
                    ydl.download([url])
                errors = 0
                break
            except youtube_dl.utils.DownloadError as e:
                if "HTTP Error 403: Forbidden" in str(e):
                    errors += 1
                    if errors == 1:
                        time.sleep(5)
                    else:
                        time.sleep(10)
                else:
                    raise