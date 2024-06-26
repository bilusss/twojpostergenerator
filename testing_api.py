

file_auth_manager = open('auth_manager.txt', 'r')
for i in file_auth_manager:
    x = i.split(sep=';')
auth_manager = SpotifyClientCredentials(x[0], x[1])
sp = spotipy.Spotify(auth_manager=auth_manager)

# Wyszukiwanie albumu
album_name = "Utopia"
result = sp.search(q='album:' + album_name, type='album')

# Pobieranie URL okładki
album_cover_url = result['albums']['items'][0]['images'][0]['url']
response = requests.get(album_cover_url)
img = Image.open(BytesIO(response.content))
img.save('album_cover.jpg')
img = Image.open('album_cover.jpg')
resized_img = img.resize((3000, 3000), Image.LANCZOS)
resized_img.save('resized_image.jpg')
resized_img.show()

