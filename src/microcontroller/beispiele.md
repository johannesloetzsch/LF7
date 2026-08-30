# µC Beispiel Setups

| Board           | Arduino-IDE | PIO                                | MicroPython | Rust |
| --------------- | ----------- | ---------------------------------- | ----------- | ---- |
|                 | [arduino.cc](https://www.arduino.cc/en/software/) | [platformio.org](https://platformio.org/)<br/>[platformio.ini](./platformio.ini) | [micropython.org](https://micropython.org/)<br/>[@Wokwi](https://wokwi.com/micropython) | [rust-embedded.org](https://docs.rust-embedded.org/book/)<br/>[@Wokwi](https://wokwi.com/rust) |
| [xiao-esp32c3](https://www.espboards.dev/esp32/xiao-esp32c3) [@Wokwi](https://wokwi.com/esp32) [@ESPHome](https://devices.esphome.io/board/esp32) ![](https://www.espboards.dev/img/xjJmXvXmqJ-200.png) | [Wokwi Template](https://wokwi.com/projects/new/esp32-c3) | `env:lolin_c3_mini`<br/>GPIO: [blink](https://github.com/platformio/platform-espressif32/tree/develop/examples/arduino-blink) | [Installation](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro), [GPIO](https://docs.micropython.org/en/latest/esp32/quickref.html#pins-and-gpio), [WiFi](https://docs.micropython.org/en/latest/esp32/quickref.html#wlan), [WebREPL](https://docs.micropython.org/en/latest/esp32/quickref.html#webrepl-web-browser-interactive-prompt), [NeoPixel](https://docs.micropython.org/en/latest/esp32/quickref.html#neopixel-and-apa106-driver) | GPIO: [blink](https://github.com/hsel-netsys/nixpkgs-esp-dev-rust/commit/10a57be89bd7644aa2fe7030f9fe5bf16e92c5b9)<br/>[![TockOS](https://tockos.org/assets/img/tock.svg)](https://tockos.org/hardware/#esp32-family) |
| [esp32-WROOM-32](https://www.espboards.dev/esp32/esp32-wroom/) [Datenblatt](https://cdn.shopify.com/s/files/1/1509/1638/files/ESP_-_32_NodeMCU_Developmentboard_Datenblatt_AZ-Delivery_Vertriebs_GmbH_10f68f6c-a9bb-49c6-a825-07979441739f.pdf?v=1598356497)<br/>[@ESPHome](https://devices.esphome.io/board/esp32) | | `env:esp-wrover-kit`<br/>GPIO: [blink](https://github.com/platformio/platform-espressif32/tree/develop/examples/arduino-blink)<br/>WiFi: [scan](https://github.com/platformio/platform-espressif32/tree/develop/examples/arduino-wifiscan) | [Installation](https://micropython.org/download/ESP32_GENERIC/) | GPIO: [blink](https://github.com/johannesloetzsch/nixpkgs-esp-dev-rust) |
| [esp8266mod-12-F](https://www.espboards.dev/esp8266/generic/) [@ESPHome](https://devices.esphome.io/board/esp8266) |             | `env:nodemcuv2`<br/>GPIO: [blink](https://github.com/platformio/platform-espressif8266/tree/develop/examples/arduino-blink)<br/>WiFi: [scan](https://github.com/platformio/platform-espressif8266/tree/develop/examples/arduino-wifiscan) |           |      |


## Hello World

```python
print("Hallo Welt")
```


### Hello Blink

```python
from machine import Pin
from time import sleep_ms

led_green = Pin(13, Pin.OUT)

while True:
    led_green.value(1)
    sleep_ms(500)
    led_green.value(0)
    sleep_ms(500)
```


### Hello 8Leds

```python
## Pinout: https://cdn.shopify.com/s/files/1/1509/1638/files/ESP_-_32_NodeMCU_Developmentboard_Datenblatt_AZ-Delivery_Vertriebs_GmbH_10f68f6c-a9bb-49c6-a825-07979441739f.pdf?v=1598356497

from machine import Pin
from time import sleep_ms

led_pins = [33, 25, 26, 27, 12, 13, 9, 10]
leds = [Pin(p, Pin.OUT) for p in led_pins]

while True:
    for value in [0, 1]:
        for led in leds:
            led.value(value)
            sleep_ms(100)
```


### Hello NeoPixel

```python
from machine import Pin
from neopixel import NeoPixel

pixels_count = 32
pixels = NeoPixel(Pin(15), pixels_count)

pixels[0] = (255, 0, 0)
pixels.write()
```


## Aufgaben

> 1. Verstehen Sie das [Beispiel um eine LED in MicroPython **blinken** zu lassen](https://wokwi.com/projects/441202072292249601).
>
> * Bauen und programmieren Sie eine kleine **Ampel**-Schaltung.

> 2. Versuchen Sie dieses [Beispiel zum Ansteuern von **NeoPixel**-LEDs mit MicroPython](https://wokwi.com/projects/441199600765977601) zu verstehen.
>
> * Wenn für das Verständnis des Programmes nötig, vereinfachen Sie den Code.
> * Spielen Sie mit dem Beispiel-Code herum und versuchen Sie neue schöne Effekte anzuzeigen.


## Rust

[Dokumentation](https://esp32.implrust.com/index.html) Rust auf dem ESP32
