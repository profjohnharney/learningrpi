# code taken from tutorial at https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat
# John Harney, 1.17.2020

from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 22)

message = "REM really were a great band."
w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x,y), message, inky_display.YELLOW, font)
inky_display.set_image(img)
inky_display.show()







