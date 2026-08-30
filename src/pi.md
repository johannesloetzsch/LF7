# Raspberry Pi
=> [Einplatinencomputer](https://de.wikipedia.org/wiki/Einplatinencomputer)


## Pinout

> **❗** Das [Pinout](https://en.wikipedia.org/wiki/Pinout) ist abhängig von der [Raspberry-Pi-Version](https://pinout.xyz/)

> **💻** Befehl um sich das Pinout eines Rapsberry-Pi auf der Kommandozeile des Pi anzeigen zu lassen:
```bash
 pinout
```

```txt
 +------------------| |--| |------+
 | ooooooooooooo P1 |C|  |A|      |
 | 1oooooooooooo    +-+  +-+      |
 |    1ooo                        |
 | P5 oooo        +---+          +====
 |                |SoC|          | USB
 |   |D| Pi Model +---+          +====
 |   |S| B  V2.0                  |
 |   |I|                  |C|+======
 |                        |S||   Net
 |                        |I|+======
 =pwr             |HDMI|          |
 +----------------|    |----------+
 
 P1:
    3V3  (1) (2)  5V    
  GPIO2  (3) (4)  5V    
  GPIO3  (5) (6)  GND   
  GPIO4  (7) (8)  GPIO14
    GND  (9) (10) GPIO15
 GPIO17 (11) (12) GPIO18
 GPIO27 (13) (14) GND   
 GPIO22 (15) (16) GPIO23
    3V3 (17) (18) GPIO24
 GPIO10 (19) (20) GND   
  GPIO9 (21) (22) GPIO25
 GPIO11 (23) (24) GPIO8 
    GND (25) (26) GPIO7
```

## GPIO Output

Die Zuordnung der externen Pin-Nummern zu den internen Nummen des Chips steht in:
`/sys/kernel/debug/gpio`

### sys-Dateisystem
Als root oder Mitglied der Gruppe `gpio`:
```bash
grep GPIO3 /sys/kernel/debug/gpio
PIN=574

echo $PIN > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio$PIN/direction

echo 1 > /sys/class/gpio/gpio$PIN/value
echo 0 > /sys/class/gpio/gpio$PIN/value
```

blink.sh
```bash
PIN=574

echo $PIN > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio$PIN/direction

while true; do
  echo 1 > /sys/class/gpio/gpio$PIN/value
  sleep 1
  echo 0 > /sys/class/gpio/gpio$PIN/value
  sleep 1
done
```

```bash
sh blink.sh
```

### Python

```bash
python  ## öffnet eine interaktive Python-Shell
```

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
PIN = 3

GPIO.setup(PIN, GPIO.OUT)

GPIO.output(PIN, True)
GPIO.output(PIN, False)

GPIO.cleanup()
```

blink.py
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED1=3
GPIO.setup(LED1, GPIO.OUT)

try:
    while(True):
        GPIO.output(LED1, True)
        time.sleep(1)
        GPIO.output(LED1, False)
        time.sleep(1)
finally:
    GPIO.cleanup()
```

```bash
python blink.py
```

### Aufgaben

> 1. Bauen Sie eine Schaltung und schreiben Sie das dazugehörige Programm, um abwechselnd 2 LEDs blinken zu lassen.
> 2. Programmieren Sie eine Ampelschaltung, die in der richtigen Reihenfolge zwischen 3 LEDs umschaltet.

### Zusatzaufgaben

> 3. Programmieren Sie eine Schaltung mit 3 LEDs, welche 3 Bits darstellen, mit denen von 0 bis 7 gezählt wird.
> 4. Schreiben Sie ein Programm, um eine 7-Segment-Anzeige anzusteuern.

## GPIO Input

### sys-Dateisystem
```bash
PIN=574
echo $PIN > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio$PIN/direction
cat /sys/class/gpio/gpio$PIN/value
```

read.sh
```bash
while true; do
  cat /sys/class/gpio/gpio$PIN/value
  sleep 1
done
```

```bash
sh read.sh
```

Die für I²C verwendeten GPIO-PINs (BCM GPIO2 und BCM GPIO3) haben einen fest verbauten Pull-Up-Widerstand.

### Python

read.py
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUTTON1=3
GPIO.setup(BUTTON1, GPIO.IN)

try:
    while(True):
        print(GPIO.input(BUTTON1))
        time.sleep(1)
finally:
    GPIO.cleanup()
```

read2.py
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUTTON1=3
GEDRUECKT=0
GPIO.setup(BUTTON1, GPIO.IN)

try:
    while(True):
        if( GPIO.input(BUTTON1) == GEDRUECKT):
            print("Button wurde gedrückt")
        else:
            print("Button wurde nicht gedrückt")
        time.sleep(1)
finally:
    GPIO.cleanup()
```

read3.py
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUTTON1=3
GEDRUECKT=0
GPIO.setup(BUTTON1, GPIO.IN)

try:
    print("Bitte Button drücken um fortzufahren…")
    while( GPIO.input(BUTTON1) != GEDRUECKT ):
        pass

    print("Bitte Button loslassen um fortzufahren…")
    while( GPIO.input(BUTTON1) == GEDRUECKT ):
        pass
finally:
    GPIO.cleanup()
    print("Das Programm ist beendet")
```

> Beispiel: [Ansteuerung mittels Webserver](https://github.com/iPlays04/led-control)

### Aufgaben

Eränzen Sie die Programme aus dem ersten Teil (GPIO Output), so dass jeweils beim Drücken eines Knopfes auf den nächsten Zustand umgeschaltet wird:

> 1. Bauen Sie eine Schaltung und schreiben Sie das dazugehörige Programm, um abwechselnd 2 LEDs blinken zu lassen.
> 2. Programmieren Sie eine Ampelschaltung, die in der richtigen Reihenfolge zwischen 3 LEDs umschaltet.

### Zusatzaufgaben

> 3. Programmieren Sie eine Schaltung mit 3 LEDs, welche 3 Bits darstellen, mit denen von 0 bis 7 gezählt wird.
> 4. Schreiben Sie ein Programm, um auf einer 7-Segment-Anzeige zu zählen.
> 5. Schreiben Sie ein Programm, das die Zeit zählt, wie lange ein Knopf gedrückt wurde.
> 6. Entwerfen Sie eine Schaltung, um mit dem Programm von 5. zu messen wie lange es dauert, einen Kondensator über einen Photoresistor zu (ent)laden.

## Weitere einfache Sensoren

### Helligkeit mit Photoresistor+Kondonsator (oder Boden-Feuchtigkeitssensor)
* [Schaltung+Library](https://gpiozero.readthedocs.io/en/stable/recipes.html#light-sensor)

### MotionSensor
* [mittels Flankenerkennung](https://tutorials-raspberrypi.de/raspberry-pi-bewegungsmelder-sensor-pir/)
* [mittels Library](https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor)
* [Beispielprojekt](https://github.com/passa-wq/SchuleBewegung)

### HC-SR04 - Ultrasonic Sensor (Entfernungsmesser)
* [Erklärung](https://www.elektronik-kompendium.de/sites/praxis/bauteil_ultrasonic-hcsr04p.htm)
* [Library](https://gpiozero.readthedocs.io/en/stable/recipes.html#distance-sensor)

## Weitere Aktuatoren/Anzeigen

### [Multi-character 7-segment display](https://gpiozero.readthedocs.io/en/stable/recipes_advanced.html#multi-character-7-segment-display)

## Parallele Protokolle

### 16x2 LCD-Display
* [Erklärung](https://tutorials-raspberrypi.de/raspberry-pi-lcd-display-16x2-hd44780/)
* [Library](https://www.instructables.com/How-to-Connect-16x2-Lcd-With-Raspberry-Pi/)

## Serielle Protokolle

### UART

```bash
minicom -D /dev/ttyUSB0

man minicom
```

```
  -D, --device
       Specify the device, overriding the value given in the configuration file.

  -b, --baudrate
       Specify the baud rate, overriding the value given in the configuration file.
```


### I²C
* Displays
* GPIO-Expander
* AD/DA-Wandler
* Microcontroller

### SPI
* Programmer z.B. für Arduino (ATtiny, ESP8266, ESP32)

### „1-Wire“ -> „Bit-Banging“
#### DHT11 / DHT22 / AM2302 (Luftfeuchtigkeit+Temperatur)
* [kurze Anleitung](https://tutorials-raspberrypi.de/raspberry-pi-luftfeuchtigkeit-temperatur-messen-dht11-dht22/)
* [ausführliche Anleitung](https://buyzero.de/blogs/news/tutorial-dht22-dht11-und-am2302-temperatursensor-feuchtigkeitsensor-am-raspberry-pi-anschliessen-und-ansteuern)

## Sonstiges

### [PiCamera](https://gpiozero.readthedocs.io/en/stable/recipes.html#button-controlled-camera)
### [SoundBoard](https://gpiozero.readthedocs.io/en/stable/recipes.html#gpio-music-box)
### [Internet connection status indicator](https://gpiozero.readthedocs.io/en/stable/recipes.html#internet-connection-status-indicator)
### [Reaction Game](https://gpiozero.readthedocs.io/en/stable/recipes.html#reaction-game)

### [Home Assistant](https://www.home-assistant.io/)
### [Raspap](https://raspap.com/)
