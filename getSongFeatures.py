import requests
import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from scipy import spatial
from stuff import *

from getSpotifySongs import userSongs


class SpotifyUserFeatures:

    @staticmethod
    def getAverageMetrics():
        s = userSongs()
        ids=s.Login()
        # pprint.pprint(ids)

        SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)  #Authenticate user
        limit = 100

        token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
        sp = spotipy.Spotify(auth=token)

        featuredValues=sp.audio_features(ids)
        #pprint.pprint(featuredValues)

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
        for elements in featuredValues:
            for key, value in elements.items():
                if value is None:
                    elements[key] = 0
            if (elements['danceability'] is None):
                elements['danceability'] = 0
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

        pprint.pprint(danceabilityVector)

        finalVector = []

        finalVector.append(sum(danceabilityVector)/limit)
        finalVector.append(sum(energyVector)/limit)
        finalVector.append(sum(keyVector)/limit)
        finalVector.append(sum(loudnessVector)/limit)
        finalVector.append(sum(modeVector)/limit)
        finalVector.append(sum(speechinessVector)/limit)
        finalVector.append(sum(acousticnessVector)/limit)
        finalVector.append(sum(instrumentalnessVector)/limit)
        finalVector.append(sum(livenessVector)/limit)
        finalVector.append(sum(tempoVector)/limit)

        # pprint.pprint(finalVector)
        #distance = 1 - spatial.distance.cosine()
        #pprint.pprint(vectors[ids[0]])

        return finalVector

# SpotifyUserFeatures.getAverageMetrics()