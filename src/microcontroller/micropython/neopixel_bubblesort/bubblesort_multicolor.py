from machine import Pin
from neopixel import NeoPixel
from random import randint

pixelCount = 64
data = [[randint(0, 256) for _ in range(3)] for _ in range(pixelCount)]

neopixel = NeoPixel(Pin(15), pixelCount)

while True:
    for color in range(3):  ## color channel to be sorted

        ## Bubblesort
        for sortedNumbers in range(len(data)-1):
            for i in range(len(data)-sortedNumbers-1):
                if data[i][color] > data[i+1][color]:
                    tmp = data[i]
                    data[i] = data[i+1]
                    data[i+1] = tmp

                    ## Display updated pixels
                    neopixel[i] = data[i]
                    neopixel[i+1] = data[i+1]
                    neopixel.write()
