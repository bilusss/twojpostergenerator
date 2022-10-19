# dimensions 3400x5000
from PIL import Image, ImageDraw, ImageFont

#   BASE - convert

img_base = Image.open('white_sheet_5000x7000.jpg')
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

myfont = ImageFont.truetype(r'LeagueGothic-Regular.ttf', size=300)
draw.text((200, 3550), "TESTING", fill=(0, 0, 0), font=myfont, spacing=10)

#   SAVE - final

img_final.save('final_resault.jpg')
img_test = Image.open('white_sheet_3300x5000.jpg')
img_test = img_test.crop((0, 0, 3200, 5000))
img_test.save('white_sheet_3200x5000.jpg')
