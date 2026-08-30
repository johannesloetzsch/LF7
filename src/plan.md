# Plan

## Zeitplan

```mermaid
gantt
 title August - September
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section Mo 31.08.
  Programmierübung Sortieren  :2026-08-31, 2h
 section Do 03.09.
  Grundlagen CPS              :2026-09-03, 5h
 section Fr 04.09.
  physikalische Betriebswerte :2026-09-04, 4h
  SOL Git                     :crit, 2026-09-04, 2h
 section Do 10.09.
  Logische Verknüpfungen      :2026-09-10, 5h
 section Fr 11.09.
  Praxis                      :2026-09-11, 4h
  SOL nandgame                :crit, 2026-09-11, 2h
```

```mermaid
gantt
 title November
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section Do 05.11.
  HTTP                        :2026-11-05, 5h
 section Fr 06.11.
  MQTT                        :2026-11-06, 4h
  SOL                         :crit, 2026-11-06, 2h
 section Do 12.11.
  Wiederholung                :2026-11-12, 5h
 section Fr 13.11.
  Klassenarbeit               :crit, 2026-11-13, 2h
  Plattformen                 :2026-11-13, 2h
  SOL                         :crit, 2026-11-13, 2h
 section Mo 16.11.
  ZQ IoT                      :2026-11-16, 8h
 section Di 17.11.
  ZQ IoT                      :2026-11-17, 8h
 section Do 19.11.
  ZQ IoT                      :2026-11-19, 8h
 section Fr 20.11.
  ZQ IoT                      :2026-11-20, 8h
```

```mermaid
gantt
 title Dezember - Januar
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section Fr 11.12.
  UART, SPI, I²C              :2026-12-11, 4h
 section Do 17.12.
  TODO                        :2026-12-17, 5h
 section Fr 18.12.
  TODO                        :2026-12-18, 4h
  SOL                         :crit, 2026-12-18, 2h
 section Di 26.01.
  Wiederholung                :2027-01-26, 5h
 section Mi 27.01.
  Klassenarbeit               :crit, 2027-01-27, 3h
```

```mermaid
gantt
 title Juni - Juli
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section Fr 18.06.
  Praxis                      :2027-06-18, 4h
  SOL                         :crit, 2027-06-18, 2h
 section Di 06.07.
  Praxis                      :2027-07-06, 3h
 section Do 08.07.
  Praxis                      :2027-07-08, 5h
```

## Leistungskontrollen

* Soll Notendichte: 7 
* Minimum Klassenarbeiten (>45min, doppelte Wertung): 2
* Sonstige Noten: >=3

> * **1. Klassenarbeit 13.11.2026** ~90min
>   * [Grundlagen CPS](grundlagen.md), [Begriffe](buzzwords.md): CPS, System, Anwendungsfelder, Technologien
>     * [Industrie 4.0](industrie40.md)
>     * [Schnittstellen](schnittstellen.md): HCI, M2M, CPS, Sensor, Aktuator
>   * [Elektrische Einheiten](einheiten.md) 
>   * [Widerstände](./resistor.md)
>     * Berechnung von (Vor-)Widerständen
>     * Pullup-/Pulldown-Wiederstände
>   * [Logische Verknüpfungen](./gatter.md) (Not, And, Or, XOr)
>     * Wahrheitswertetabelle
>     * Schaltung mit einfachen (Um-)Schaltern
>   * [Rechnen mit Binärzahlen, Zweierpotenzen](binary.md)
>   * [Grundlagen Git](./git.md)
>     * [DevOps](devops.md)
>   * [HTTP](http.md), [MQTT](mqtt.md)

> * **2. Klassenarbeit 27.01.2027** ~90min
>   * Auswahl [Hardwareplattformen und Programmiersprachen](./microcontroller/beispiele.md)
>   * [Rechnernetze / Topologien](rechnernetze.md)
>   * [OSI-Modell](osi.md) (insbesondere Physical Layer und anwendungsorientierte Protokolle)
>   * [UART](bituebertragung.md#uart), [SPI](rechnernetze.md#spi), [I²C](rechnernetze.md#i²c)
>   * Grundlagen Programmierung (Variablen, Datenstrukturen, Schleifen, Bedingungen, Funktionen)
>     * Siehe Programmierbeispiele [Pi](pi.md), [I²C-Beispiel (main.py)](rechnernetze.md#i²c)

Programmier-Übungsaufgaben:
* Blink [Pi Pico](https://wokwi.com/projects/300504213470839309), [ESP32](https://wokwi.com/projects/359801682833812481)
* [Ampel](https://wokwi.com/projects/432915684639002625)
* [Buzzer](https://wokwi.com/projects/432915379839949825)
* [Button](https://wokwi.com/projects/432915323107785729)
* [7-Segment + Schalter](https://wokwi.com/projects/300210834979684872)

> * **Mündliche Note**
>   * Vorstellung Projektplan
>   * Bisherige Mitarbeit

> * **Bewertung Praxisprojekt**
>   * **Note für fachliche Leistung**
>   * **Note für Mitarbeit**
> * Projektpräsentation
