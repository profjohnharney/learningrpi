# attempt to get Kylo Ren on the InkyPHAT

from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

inky_display = InkyPHAT("yellow")
# inky_display.set_border(inky_display.WHITE)

img = Image.open("kylo.png")
inky_display.set_image(img)
inky_display.show()
