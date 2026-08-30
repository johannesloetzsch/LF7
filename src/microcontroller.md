# [Mikrocontroller](https://de.wikipedia.org/wiki/Mikrocontroller)
(µController, µC, MCU, „**Einchipmikrorechner**“)

* Prozessor
* RAM
* [**Flash**-EEP**ROM**](https://de.wikipedia.org/wiki/Flash-Speicher)


## [Beispiele bekannter Mikrocontroller](https://de.wikipedia.org/wiki/Liste_von_Mikrocontrollern)
* Atmel [ATtiny, ATmega](https://de.wikipedia.org/wiki/Microchip_AVR)
  * 8bit AVR

* Espressif [ESP8266](https://de.wikipedia.org/wiki/ESP8266) ([NodeMCU](https://de.wikipedia.org/wiki/NodeMCU)), [ESP32](https://de.wikipedia.org/wiki/ESP32)
  * 32bit Wi-Fi Controller (Xtensa LX6 oder RISC-V)

* Raspberry Pi Foundation [RP2040](https://de.wikipedia.org/wiki/RP2040)
  * 32bit ARM Cortex-M0+

* STMicroelectronics [STM32](https://en.wikipedia.org/wiki/STM32)
  * 32bit ARM Cortex-M


## Mikrocontroller vs [SoC](https://de.wikipedia.org/wiki/System-on-a-Chip) vs Einplatinencomputer

> **💡** Videoerklärung zu [Mikrocontroller](https://www.youtube.com/watch?v=xd6oA8UiG7s) und [SoC](https://www.youtube.com/watch?v=L4XemL7t6hg)

<iframe width="560" height="315" src="https://www.youtube.com/embed/xd6oA8UiG7s?si=Y36Kbizlt9FrauM9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/L4XemL7t6hg?si=cNZkbTtw4UWiG7ta" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Mikrocontroller
>Vorteile:
>1.	Kostengünstig: Microcontroller werden in kostensensitiven Projekte eingesetzt.
>2.	Energieeffizient: Sie verbrauchen wenig Strom, was sie perfekt für batteriebetriebene Anwendungen macht.
>3.	Einfache Integration: Microcontroller sind oft leicht in bestehende Systeme zu integrieren und benötigen nur minimale externe Komponenten.

>Nachteile:
>1.	Begrenzte Rechenleistung: Sie haben weniger Rechenleistung und Speicher im Vergleich zu Einplatinencomputern.
>2.	Eingeschränkte Funktionalität: Microcontroller sind für spezifische Aufgaben ausgelegt und bieten weniger Flexibilität für komplexe Anwendungen.
>3.	Weniger Peripherieoptionen: Sie haben oft weniger Schnittstellen und Peripheriegeräte im Vergleich zu Einplatinencomputern.

## [SoC](https://de.wikipedia.org/wiki/System-on-a-Chip)
**S**ystem-**o**n-a-**C**hip

>Vorteile:
>1. Hohe Integration: CPU, GPU, Speicher, und Peripheriegeräte auf einem Chip (kompakte Bauweise).
>2. Energieeffizienz: Optimierter Stromverbrauch durch Integration und geringere Kommunikationsverluste.
>3. Leistungsfähigkeit: Häufig leistungsstärker als Mikrocontroller, geeignet für komplexe Anwendungen (z. B. Multimedia, AI).

>Nachteile:
>1. Komplexität: Höhere Anforderungen an Design und Programmierung als bei Mikrocontrollern.
>2. Kosten: Teurer als Mikrocontroller, insbesondere bei kleinen Projekten oder niedrigen Stückzahlen.
>3. Reparatur/Austausch: Fehlfunktion einzelner Komponenten kann den Austausch des gesamten Chips erfordern.

## Einplatinencomputer

>Vorteile:
>1.	Hohe Rechenleistung: Einplatinencomputer wie der Raspberry Pi bieten deutlich mehr Rechenleistung und Speicher.
>2.	Vielseitigkeit: Sie können eine Vielzahl von Betriebssystemen ausführen und sind für komplexe Anwendungen geeignet.
>3.	Erweiterbarkeit: Einplatinencomputer bieten zahlreiche Schnittstellen und Peripheriegeräte, was sie sehr flexibel macht.

>Nachteile:
>1.	Höherer Stromverbrauch: Sie verbrauchen mehr Strom als Microcontroller, was sie weniger geeignet für batteriebetriebene Anwendungen macht.
>2.	Kosten: Einplatinencomputer sind in der Regel teurer als Microcontroller.
>3.	Komplexität: Die Einrichtung und Programmierung kann komplexer sein, was eine steilere Lernkurve bedeutet.


## Für Mikrocontroller häufig verwendete Programmiersprachen

* C, C++ ([*Ardu*ino *Sketches*](https://docs.arduino.cc/learn/programming/sketches/))
* [Rust](https://docs.rust-embedded.org/book/)
* [MicroPython](https://docs.micropython.org/en/latest/esp32/quickref.html)

> **❓❗💬** Erklären Sie, welche Eigenschaften, Vor-/Nachteile und Einsatzzwecke die verschiedenen Programmiersprachen haben.

## [Arduino](https://docs.arduino.cc/programming/)
* [Language Reference](https://docs.arduino.cc/language-reference/)
* [Libraries](https://reference.arduino.cc/reference/en/libraries/)
* [Beispiele](https://docs.arduino.cc/built-in-examples/)
* [Tutorials](https://docs.arduino.cc/learn/starting-guide/getting-started-arduino/) […](https://www.tutorialspoint.com/arduino/)
* [Projekte](https://projecthub.arduino.cc/), […](https://www.instructables.com/Arduino-Projects/)


## Programmer und IDEs für Arduino

* [Arduino IDE](https://docs.arduino.cc/software/ide/)
* [PlatformIO](https://platformio.org/)

```bash
pio device list

git clone https://github.com/platformio/platform-espressif8266  ## oder platform-espressif32
cd platform-*/examples/arduino-wifiscan
pio run --target upload -e nodemcuv2  ## für esp8266mod-12-F
pio run --target upload -e esp-wrover-kit  ## für esp-WROOM-32

pio device monitor -b 115200
```

[platformio.ini](./microcontroller/platformio.ini) für die ESPs der Schule


## **💡** [Simulator](https://wokwi.com/)
