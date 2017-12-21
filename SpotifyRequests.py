import requests
from scipy import spatial
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import json
import operator

from MusicTechHackathon2k17.getSongFeatures import SpotifyUserFeatures


class SpotifyRequests:
    LIMIT = 100

    def get_place_top_songs_names_artists(self):
        client_credentials_manager = SpotifyClientCredentials(SpotifyRequests.SPOTIPY_CLIENT_ID, SpotifyRequests.SPOTIPY_CLIENT_SECRET)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        username = "thesoundsofspotify"
        playlists = {}

        results = sp.user("thesoundsofspotify")
        # pprint(results)
        count = 0
        for place in open("places.txt"):
            place_q = place.replace(",", "")
            playlist_name = "The Sound of " + place_q + " US"
            count+=1
            playlist = sp.search(playlist_name, type="playlist")
            if len(playlist['playlists']['items']) > 0:
                playlists[place] = []
                tracks = sp.user_playlist_tracks(username, playlist['playlists']['items'][0]['uri'].split(':')[4], limit=SpotifyRequests.LIMIT)
                for element in tracks['items']:
                    song_artist = element['track']['name'] + ', ' + element['track']['artists'][0]['name']
                    playlists[place].append(song_artist)

        with open('topSongPerPlace.txt', 'w') as file:
            file.write(json.dumps(playlists))

    def get_place_top_songs_ids(self):
        client_credentials_manager = SpotifyClientCredentials(SpotifyRequests.SPOTIPY_CLIENT_ID, SpotifyRequests.SPOTIPY_CLIENT_SECRET)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        username = "thesoundsofspotify"
        playlists = {}

        results = sp.user("thesoundsofspotify")
        count = 0
        for place in open("places.txt"):
            playlist_name = "The Sound of " + place + " US"
            count+=1
            playlist = sp.search(playlist_name, type="playlist")
            if len(playlist['playlists']['items']) > 0:
                playlists[place] = []
                tracks = sp.user_playlist_tracks(username, playlist['playlists']['items'][0]['uri'].split(':')[4], limit=SpotifyRequests.LIMIT)
                for element in tracks['items']:
                    song_id = element['track']['id']
                    playlists[place].append(song_id)

        with open('topSongIdsPerPlace.txt', 'w') as file:
            file.write(json.dumps(playlists))

    def generate_vectors(self, top_five_file):
        # Make sure the top_five_file is full of song IDs
        places = {}


        for line in open(top_five_file):
            songs = json.loads(line)
        for key, value in songs.items():
            danceabilityVector = [];
            energyVector = [];
            keyVector = [];
            loudnessVector = [];
            modeVector = [];
            speechinessVector = [];
            acousticnessVector = [];
            instrumentalnessVector = [];
            livenessVector = [];
            valenceVector = [];
            tempoVector = [];

            finalVector = []

            client_credentials_manager = SpotifyClientCredentials(SpotifyRequests.SPOTIPY_CLIENT_ID, SpotifyRequests.SPOTIPY_CLIENT_SECRET)
            sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
            results = sp.audio_features(value)

            for elements in results:
                danceabilityVector.append(elements['danceability'])
                energyVector.append(elements['energy'])
                keyVector.append(elements['key'])
                loudnessVector.append(elements['loudness'])
                modeVector.append(elements['mode'])
                speechinessVector.append(elements['speechiness'])
                acousticnessVector.append(elements['acousticness'])
                instrumentalnessVector.append(elements['instrumentalness'])
                livenessVector.append(elements['liveness'])
                valenceVector.append(elements['valence'])
                tempoVector.append(elements['tempo'])
            # places['key'].append() # should point to the average vector of that place
            finalVector.append(sum(danceabilityVector)/5)
            finalVector.append(sum(energyVector)/5)
            finalVector.append(sum(keyVector)/5)
            finalVector.append(sum(loudnessVector)/5)
            finalVector.append(sum(modeVector)/5)
            finalVector.append(sum(speechinessVector)/5)
            finalVector.append(sum(acousticnessVector)/5)
            finalVector.append(sum(instrumentalnessVector)/5)
            finalVector.append(sum(livenessVector)/5)
            finalVector.append(sum(tempoVector)/5)

            places[key] = finalVector
        # pprint(places)
        with open ('PlaceToAverageSongMetrics.txt', 'w') as file:
            file.write(json.dumps(places))
        return places

    def similarity_calculations(self):
        user_vector = SpotifyUserFeatures.getAverageMetrics()
        for line in open('PlaceToAverageSongMetrics.txt', 'r'):
            places = json.loads(line)
        similarities = {}
        for key, value in places.items():
            similarities[key] = 1 - spatial.distance.cosine(value, user_vector)
        similarity_sorts = sorted(similarities.items(), key=operator.itemgetter(1))

        pprint(similarity_sorts)


bull = SpotifyRequests()
bull.get_place_top_songs_names_artists()
bull.get_place_top_songs_ids()
bull.generate_vectors('topSongIdsPerPlace.txt')
bull.similarity_calculations()