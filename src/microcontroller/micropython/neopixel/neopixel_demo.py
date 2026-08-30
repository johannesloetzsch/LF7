from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

pixels_count = 32
pixels = NeoPixel(Pin(15), pixels_count)
pixels_count_half = int(pixels_count/2)


def color_by_position(offset_unlimited):
    ## This function accepts any values as offset.
    ## For the following calculation we limit offset to be a value between 0 and pixels_count
    offset = offset_unlimited % pixels_count

    ## brightness should be a value between 0 and 1
    ## in this example we use a linear interpolation from 0 via 1 to 0
    brightness = abs(offset-pixels_count_half) / pixels_count_half

    ## The result is a 8bit integer and can be used as rgb-color-component
    return int(255*brightness)


t = 0
while True:
    t += 1

    for i in range(pixels_count):
        r = color_by_position(i-t)
        g = color_by_position(i-t + int(pixels_count*1/3))
        b = color_by_position(i-t + int(pixels_count*2/3))
        pixels[i] = (r, g, b)

    pixels.write()
    sleep_ms(100)
