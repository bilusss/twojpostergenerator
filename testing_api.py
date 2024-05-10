import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from PIL import Image
"""
auth_manager = SpotifyClientCredentials('5d1e4fbae1f946c9988e4e7c68767b0b','b6c5324495f74797971deaf349a9a03a')
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('g08j1jjjbl1dvybddj18802ov')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
###########
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
###########
"""
auth_manager = SpotifyClientCredentials('5d1e4fbae1f946c9988e4e7c68767b0b','b6c5324495f74797971deaf349a9a03a')
sp = spotipy.Spotify(auth_manager=auth_manager)

#   playlisty norka

# playlists = sp.user_playlists('g08j1jjjbl1dvybddj18802ov')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None

#   Artist followers and URI

artist_name = "A$AP Rocky" #input("Name of the artist: ")
q_ = "artist:<"+artist_name+">"
a = sp.search(q=q_, type='artist', limit=1)
print(f"\n{artist_name} has {a['artists']['items'][0]['followers']['total']:,} followers on Spotify!")
print(f"{artist_name}'s URI - {a['artists']['items'][0]['id']}")

#   album cover

lz_uri = a['artists']['items'][0]['id']

results = sp.artist_top_tracks(lz_uri)
print(results)

for track in results['tracks'][:1]:
    print(f"track    : {track['name']}")
    print(f"audio    : {track['preview_url']}")
    print(f"cover art: {track['album']['images'][0]['url']}")
    coverart = track['album']['images'][0]['url']
    print()


def fetch_image(url):
    img_data = requests.get(url).content
    with open('coverart.jpg', 'wb') as handler:
        handler.write(img_data)
    # print(url)
    # response = requests.get(url)
    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     img_tag = soup.find('img')
    #     if img_tag:
    #         img_src = img_tag['src']
    #         img_response = requests.get(img_src)
    #         if img_response.status_code == 200:
    #             img = Image.open(BytesIO(img_response.content))
    #             img.show()
    #         else:
    #             print("Unable to fetch the image.")
    #     else:
    #         print("No image found on the webpage.")
    # else:
    #     print("Unable to fetch the webpage content.")

def rescale_img(path):


url = coverart
fetch_image(url)
rescale_img("coverart.jpg")



"""
b = sp.artist_albums(artist_id=a['artists']['items'][0]['id'],limit=50)
album_name = "testing"#input("Name of the artist: ")
q_2 = "album:<"+album_name+">"
b = sp.search(q=q_2, type='album', limit=1)
print(a['artists']['items'][0]['id'])
print()
print(sp.album_tracks(album_id=b,limit=1))
"""