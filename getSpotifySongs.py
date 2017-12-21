import requests
import spotipy
import sys
import spotipy.util as util
import pprint
from stuff import *

from spotipy.oauth2 import SpotifyClientCredentials


class userSongs:
    def Login(self):
        scope = 'user-top-read'
        SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
        token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
        # pprint.pprint(token)
        sp = spotipy.Spotify(auth=token)        #creates "spotify object"
        # pprint.pprint(sp.current_user())
        tracks=sp.current_user_top_tracks(limit=100) #takes user's top tracks from spotify object

        # pprint.pprint(tracks)

        ids = []
        for element in tracks['items']:
            ids.append(element['id'])
            # print(element['id'])

        return ids