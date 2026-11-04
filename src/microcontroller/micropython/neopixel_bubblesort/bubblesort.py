from machine import Pin
from neopixel import NeoPixel  ## https://docs.micropython.org/en/latest/library/neopixel.html
from random import randint
from time import sleep_ms

pixelCount = 64
data = [randint(0, 256) for _ in range(pixelCount)]

neopixel = NeoPixel(Pin(15), pixelCount)

## Bubblesort
for sortedNumbers in range(len(data)-1):
    for i in range(len(data)-sortedNumbers-1):
        if data[i] > data[i+1]:
            tmp = data[i]
            data[i] = data[i+1]
            data[i+1] = tmp

            ## Display updated values as green pixels
            neopixel[i] = [0, data[i], 0]
            neopixel[i+1] = [0, data[i+1], 0]
            neopixel.write()
        sleep_ms(100)
