import requests
import spotipy
from bs4 import BeautifulSoup
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "7bc27c78ffdd49d7839ad078898c9e93"
CLIENT_SECRET = "f6da3323c8aa4fbd8efee971baece9a9"
REDIRECT_URI = "http://example.com"
SPOTIFY_ENDPOINT = "https://api.spotify.com/v1"
TOKEN = ("XXXXXXX")

user_input = input("Which year do you want travel back in time? Type de date in this format YYYY-MM-DD:")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_input}/")
content = response.text

soup = BeautifulSoup(content, "lxml")
title_of_story = soup.select("ul li ul h3")
list_of_songs = [title.string.strip("\n\t") for title in title_of_story]
print(list_of_songs)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="gabrielcoelhocn08"))

user_id = sp.current_user()['id']
tracks_play = []
for song in list_of_songs:
    src = sp.search(f"{song}", 1, 0, "track")
    title = src['tracks']['items'][0]['uri']
    tracks_play.append(title)

playlist_create = sp.user_playlist_create(f"{user_id}", name="Allie's birthday songs", public=False,
                                          description="playlist created by a past date")

add_songs = sp.playlist_add_items(playlist_id=playlist_create["id"], items=tracks_play, position=None)


