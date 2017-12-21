#  Client Keys
CLIENT_ID = "<client_id>"
CLIENT_SECRET = "<client_secret>"

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8080
REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "playlist-modify-public playlist-modify-private"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

#User info
scope = 'user-top-read'
username = '<username>'
SPOTIPY_CLIENT_ID='<Spotipy_client_id>'
SPOTIPY_CLIENT_SECRET='<Spotipy_client_secret>'
SPOTIPY_REDIRECT_URI='<Spotipy_redirect_url>'
