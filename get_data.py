import pandas as pd
import sys
import spotipy

client_id = 'ID_GOES_HERE'
client_secret = 'ID_SECRET_GOES_HERE'

from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public user-top-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def get_top_100_artists(time_range='medium_term'):
    """
    time_range options: 'short_term' (~4 weeks), 'medium_term' (~6 months), 'long_term' (years)
    """
    top_artists = []

    # Spotify API limits each request to 50 items
    for offset in [0, 50]:
        results = sp.current_user_top_artists(
            limit=50,
            offset=offset,
            time_range=time_range
        )
        top_artists.extend(results['items'])

    return top_artists

'''
# Execution
artists_100 = get_top_100_artists()
for i, artist in enumerate(artists_100, 1):
    print(f"{i}. {artist['name']}")
    '''

top_tracks = sp.current_user_top_tracks(time_range='medium_term', limit=50)
for item in top_tracks['items']:
    print(item['name'])
