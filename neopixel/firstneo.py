# this is all from Adafruit (https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage)

import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 5)

# pixels[0] = (255, 0, 0)

pixels.fill((0, 255, 0))
