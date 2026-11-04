from machine import Pin
from neopixel import NeoPixel
from random import randint
from time import sleep_ms


PIXEL_COUNT = 64
LED_PIN = 15

SORT_DELAY_MS = 15
PAUSE_AFTER_SORT_MS = 1500


neopixel = NeoPixel(Pin(LED_PIN), PIXEL_COUNT)


def random_dominant_color():
    """
    Create a color with one clearly dominant RGB channel.
    """
    dominant_channel = randint(0, 2)

    max_nondominant = randint(100, 255)  ## this 2 parameters can be tuned
    
    color = [
        randint(0, max_nondominant),
        randint(0, max_nondominant),
        randint(0, max_nondominant),
    ]

    color[dominant_channel] = randint(max_nondominant, 255)

    return tuple(color)


def create_data():
    return [
        random_dominant_color()
        for _ in range(PIXEL_COUNT)
    ]


def bubble_sort_by_channel(data, channel):
    for sorted_numbers in range(len(data) - 1):
        for i in range(len(data) - sorted_numbers - 1):
            if data[i][channel] > data[i + 1][channel]:
                data[i], data[i + 1] = data[i + 1], data[i]

                # Only update the two pixels that changed
                neopixel[i] = data[i]
                neopixel[i + 1] = data[i + 1]
                neopixel.write()

                sleep_ms(SORT_DELAY_MS)


data = create_data()
while True:
    for color_to_be_sorted in range(3):
        bubble_sort_by_channel(data, color_to_be_sorted)
        sleep_ms(PAUSE_AFTER_SORT_MS)
