# Plan

## Zeitplan

```mermaid
gantt
 title August (15h)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section 2h Do 22.08.
  Einführung                  :2024-08-22, 2h
 section 4h Fr 23.08.
  Grundlagen CPS, SOL (Funktionsweise CPU)  :2024-08-23, 4h
 section 5h Do 29.08.
  Logische Verknüpfungen, Binäres Rechnen, Praxis Logische Verknüpfungen  :2024-08-29, 5h
 section 4h Fr 30.08.
  Von-Neumann-Zyklus          :2024-08-30, 4h
```
```mermaid
gantt
 title Oktober + November (12h)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section 3h Mo 21.10.
  Einführung Mikrocontroller  :2024-10-21, 3h
 section 3h Mi 30.10.
  Praxis Arduino (Simulator)  :2024-10-24, 3h
 section 4h Fr 01.11.
  Einführung Git              :2024-11-01, 2h
  SOL (Git)                   :2024-11-01, 2h
```
```mermaid
gantt
 title Dezember (17h)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section 5h Do 05.12.
  Physikalische Betriebswerte, Berechnung von (Vor-)Widerständen  :2024-12-05, 4h
 section 4h Fr 06.12.
  Wiederholung                :2024-12-06, 2h
  SOL (Rechnernetze / Topologien + Vorbereitung Klassenarbeit)  :2024-12-06, 2h
 section 2h Di 10.12.
  Fragen zur Klassenarbeit    :2024-12-10, 2h
 section 2h Mi 11.12.
  Klassenarbeit               :milestone, 2024-12-11, 2h
```
```mermaid
gantt
 title Januar (13h)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section 3h Do 22.01.
  OSI-Modell (Physical Layer) :2025-01-23, 3h
 section 5h Do 23.01.
  UART, I²C, SPI              :2025-01-23, 5h
 section 4h Fr 24.01.
  HTTP, MQTT                  :2025-01-24, 2h
  SOL (Vorbereitung Klassenarbeit)  :2025-01-24, 2h
 section 3h Di 28.01.
  Wiederholung                :2025-01-23, 3h
 section 4h Fr 31.01.
  Klassenarbeit               :milestone, 2025-01-31, 2h
  SOL (Projektplanung)        :2025-01-31, 2h
```
```mermaid
gantt
 title März (6h)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section 2h Mi 19.03.
  Praxisprojekt               :2025-03-19, 2h
 section 4h Fr 21.03.
  …                           :2025-03-21, 2h
  SOL                         :2025-03-21, 2h
```
```mermaid
gantt
 title Juni (28h)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section 3h Mi 04.06.
  HTTP, MQTT                  :2025-06-04, 3h
 section 5h Do 05.06.
  UART, I²C, SPI              :2025-06-05, 5h
 section 5h Do 19.06.
  Wiederholung Klassenarbeit  :2025-06-19, 5h
 section 2h Fr 20.06.
  Klassenarbeit               :2025-06-20, 2h
 section 4h Fr 20.06.
  Praxisprojekt               :2025-06-20, 4h
 section 2h Fr 20.06.
  SOL (Projektdokumentation)  :2025-06-20, 2h
 section 3h Mo 23.06.
  Projektabschluss            :2025-06-23, 3h
 section 4h Fr 27.06.
  Projektvorstellungen        :2025-06-27, 4h
```

## Leistungskontrollen

* Soll Notendichte: 7 
* Minimum Klassenarbeiten (>45min, doppelte Wertung): 2
* Sonstige Noten: >=3

> * **1. Klassenarbeit 11.12.** ~90min (einseitig beschrifteter A4 Notizzettel + 1 einfacher Taschenrechner ohne Binärberechnungen)
>   * [Grundlagen CPS](grundlagen.md), einschließlich [Schnittstellen](schnittstellen.md)
>   * [Rechnen mit Binärzahlen, Zweierpotenzen](binary.md)
>   * [Logische Verknüpfungen](./prozessor.md#Logikgatter) (Not, And, Or, XOr)
>     * Wahrheitswertetabelle
>     * Logik Gatter (Schaltung mit einfachen (Um-)Schaltern)
>   * ~~Von-Neumann-Zyklus~~
>   * Berechnung von (Vor-)Widerständen
>   * [Rechnernetze / Topologien](rechnernetze.md)
>   * [Grundlagen Git](./git.md)

> * **2. Klassenarbeit 20.06.** (1.+2. UE) ~90min (einseitig beschrifteter A4 Notizzettel)
>   * OSI-Modell (insbesondere Physical Layer und anwendungsorientierte Protokolle)
>   * UART, I²C, SPI
>   * HTTP, MQTT
>   * Grundlagen Programmierung (Variablen, While, If/Else)
