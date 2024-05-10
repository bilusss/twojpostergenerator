# dimensions 3400x5000
from PIL import Image, ImageDraw, ImageFont
import PIL
from collections import Counter
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

#   SPOTIFY API

file_auth_manager = open('auth_manager.txt', 'r')
for i in file_auth_manager:
    x = i.split(sep=';')
auth_manager = SpotifyClientCredentials(x[0], x[1])
sp = spotipy.Spotify(auth_manager=auth_manager)

# name
artist_name = "a$ap rocky" #    input("Artist name: ") #a$ap rocky, travis scott
q = "artist:<"+artist_name+">"
a = sp.search(q=q, type='artist', limit=1)
artist_uri = a['artists']['items'][0]['id']

b = sp.artist(artist_uri)
artist_name = b['name']# overwriting artist's name
print("artist's name :", artist_name)
print("artist's id   :", artist_uri)

# album

def Label(s: str):
    if "record" in s.lower():
        ind = s.lower().index("record")
        for i in range(ind, len(s)):
            if s[i] == " ":
                ind = i
                break
        s = s[:ind]
    for i in range(len(s)-3):
        try:
            if 2030>=int(s[i:i+4])>=1000:
                s=s[i+5:]
                break
        except ValueError:
            pass
    return s




album_name = "testing" #    input("Album name: ") #testing, utopia
q = "album:<"+album_name+">"+" "+"artist:<"+artist_name+">"
c = sp.search(q=q, type='album', limit=1)
album_id = c['albums']['items'][0]['id']
d = sp.album(album_id=album_id)
album_name = d['name']
released_by = d['copyrights'][0]['text']
print("album's name  :", album_name)
print("album's id    :", album_id)
print("released by   :", Label(released_by))

# released date
released_date = c['albums']['items'][0]['release_date']
print("released date :", released_date)

# tracks
album_tracks_data = sp.album_tracks(album_id=album_id,market="US", limit=50)

print("tracklist     :", end=" ")
tracklist = []
for count, x in enumerate(album_tracks_data['items'], 1):
    if count > 1:
        tracklist.append(x['name'])
        print("               ", count, x['name'])
        continue
    print(count, x['name'], " ")

#   BASE - convert

img_base = Image.open('5000x7000_base.png')
left, upper, right, lower = 0, 0, 3400, 5600
img_base = img_base.crop((left, upper, right, lower))
img_base.save('white_sheet_final_3400x5600.jpg')
img_final = Image.open('white_sheet_final_3400x5600.jpg')

#   BASE - outdraw

draw = ImageDraw.Draw(img_final)
draw.line((24, 0, 24, 5600), fill=(0, 0, 0), width=51)
draw.line((50, 5575, 3400, 5575), fill=(0, 0, 0), width=50)
draw.line((3375, 5575, 3375, 0), fill=(0, 0, 0), width=50)
draw.line((3350, 25, 0, 25), fill=(0, 0, 0), width=50)

#   PASTE - album cover

img_cover = Image.open('rocky_testing.jpg')
img_final.paste(img_cover, (200, 250))

#   UNDERLINE - draw

draw.line(((200, 3400), (3200, 3400)), fill=(0, 0, 0), width=10)

#   TEXT - album title

title_font = ImageFont.truetype(r'LeagueGothic-Regular.ttf', size=300)
draw.text((200, 3550), album_name, fill=(0, 0, 0), font=title_font, spacing=10)

#   TEXT - artist nickname

artist_font = ImageFont.truetype(r'LeagueGothic-CondensedRegular.ttf', 250)
draw.text((220, 3850),artist_name, fill=(0,0,0), font=artist_font, spacing=10)

#   TEXT - release date

release_date_font = ImageFont.truetype(r'LTSuperiorMono-Regular.otf', 120)
draw.text((220,4150), "Release date:", fill=(0,0,0), font=release_date_font, spacing=0)

#   TEXT - date

date_font = ImageFont.truetype(r'LeagueGothic-Regular.ttf', 150)
draw.text((220,4300), released_date, fill=(0,0,0), font=date_font, spacing=0)

#   TEXT - released by

released_by_font = ImageFont.truetype(r'LTSuperiorMono-Regular.otf', 120)
draw.text((220,4550), "Released by:", fill=(0,0,0), font=released_by_font, spacing=0)

#   TEXT - label

label = ImageFont.truetype(r'LeagueGothic-Regular.ttf', 150)
draw.text((220,4700), "A$AP Rocky Recordings", fill=(0,0,0), font=label, spacing=0)

#   SPOTIFY

def fetch_image(url):
    img_data = requests.get(url).content
    with open('spotify_code.jpg', 'wb') as handler:
        handler.write(img_data)

url = "https://scannables.scdn.co/uri/plain/jpeg/FFFFFF/black/640/spotify:album:"+album_id
fetch_image(url)
spotify_code = Image.open('spotify_code.jpg')
img_final.paste(spotify_code, (220, 4900))

#   COLORS

def myround(x, base=5):
    return base * round(x/base)

pixels = img_cover.load()
width, height = img_cover.size
colors = []
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        r, g, b = myround(r), myround(g), myround(b)
        colors.append((r, g, b))
counter = Counter(colors)
def color_difference(color1, color2, threshold=40):
    return any(abs(c1 - c2) >= threshold for c1, c2 in zip(color1, color2))

most_common_colors = []
for color, count in counter.most_common():
    if len(most_common_colors) == 5:
        break
    if all(color_difference(color, c) for c in most_common_colors):
        most_common_colors.append(color)

for i in range(5):
    draw.rectangle(xy=(220+150*i, 5100, 370+150*i, 5250), fill=most_common_colors[i])

#   TEXT - Tracklist

def featstrip(s: str):
    if "(feat" in s:
        ind_s = s.index("(feat")
        s_ = s[0:ind_s-1]
        return s_
    if "(with" in s:
        ind_s = s.index("(with")
        s_ = s[0:ind_s-1]
        return s_
    return s

tracklist_font = ImageFont.truetype(r'LTSuperiorMono-Regular.otf', 70)

tracklisttextall = ""
for i in range(len(tracklist)):
    text = str(i+1)+"."+featstrip(tracklist[i])+"\n"
    tracklisttextall+=text
draw.text((1700,3650+i), tracklisttextall, fill=(0,0,0), font=tracklist_font, spacing=10)

#   SAVE - final

img_final.save('final_result.jpg')
