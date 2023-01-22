import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Set up the SpotifyOAuth object with your Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='-',
                                              client_secret='-',
                                              redirect_uri='http://localhost:8000/callback',
                                              username='-'))
# Get the playlists for the authenticated user
playlists = sp.current_user_playlists()

# Set the file path to the C drive
# Set the file path to the C drive
file_path = os.path.join("C:\\", "Users", "Iccanui", "Desktop", "playlists.txt")


# Open the file for writing with utf-8 encoding
with open(file_path, "w", encoding='utf-8') as f:
    # Iterate over the playlists and write their information to the file
    for playlist in playlists['items']:
        f.write(playlist['name'] + '\n')
        tracks = sp.playlist_tracks(playlist['id'])
        for track in tracks['items']:
            f.write("- " + track['track']['name'] + ' by ' + track['track']['artists'][0]['name'] + '\n')
