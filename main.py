# dimensions 3400x5000
from PIL import Image, ImageDraw, ImageFont
import PIL
from collections import Counter

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
draw.text((200, 3550), "TESTING", fill=(0, 0, 0), font=title_font, spacing=10)

#   TEXT - artist nickname

artist_font = ImageFont.truetype(r'LeagueGothic-CondensedRegular.ttf', 250)
draw.text((220, 3850),"A$AP Rocky", fill=(0,0,0), font=artist_font, spacing=10)

#   TEXT - release date

release_date_font = ImageFont.truetype(r'LTSuperiorMono-Regular.otf', 120)
draw.text((220,4150), "Release date:", fill=(0,0,0), font=release_date_font, spacing=0)

#   TEXT - date

date_font = ImageFont.truetype(r'LeagueGothic-Regular.ttf', 150)
draw.text((220,4300), "25.05.2018", fill=(0,0,0), font=date_font, spacing=0)

#   TEXT - released by

released_by_font = ImageFont.truetype(r'LTSuperiorMono-Regular.otf', 120)
draw.text((220,4550), "Released by:", fill=(0,0,0), font=released_by_font, spacing=0)

#   TEXT - label

label = ImageFont.truetype(r'LeagueGothic-Regular.ttf', 150)
draw.text((220,4700), "A$AP Rocky Recordings", fill=(0,0,0), font=label, spacing=0)

#   Spotify scan

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


#   SAVE - final

img_final.save('final_result.jpg')
# img_test = Image.open('white_sheet_3300x5000.jpg')
# img_test = img_test.crop((0, 0, 3200, 5000))
# img_test.save('white_sheet_3200x5000.jpg')
