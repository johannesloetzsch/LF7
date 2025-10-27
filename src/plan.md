# Plan

## Zeitplan

```mermaid
gantt
 title August - September (20UE LF7)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section Do 28.08. 5
  Einführung, Grundlagen CPS, Schnittstellen, Einheiten  :2025-08-28, 5h
 section Fr 29.08. 6
  Widerstände, Logikgatter, Binäres Rechnen, DevOps  :2025-08-29, 4h
  SOL Git                     :crit, 2025-08-29, 2h
 section Do 04.09. 5
  Q&A, Wiederholung           :2025-09-04, 5h
  Nachhilfe                   :2025-09-04, 2h
 section Fr 05.09. 4
  Klassenarbeit               :crit, 2025-09-05, 2h
  GPIO, Mikrocontroller, Raspberry Pi, Simulator  :2025-09-05, 2h
```

```mermaid
gantt
 title Oktober (38UE IoT + 3UE LF7 + 11UE LF8)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section Mo 20.10. 8
  IoT Kurs                    :2025-10-20, 8h
 section Di 21.10. 8
  IoT Kurs                    :2025-10-21, 8h
 section Mi 22.10. 8
  IoT Kurs                    :2025-10-22, 8h
 section Do 23.10. 8
  IoT Kurs                    :2025-10-23, 8h
 section Fr 24.10. 6
  IoT Kurs                    :2025-10-24, 6h
 section Di 28.10. 3
  Standards, Node-RED, HTTP   :2025-10-28, 3h
 section Mi 29.10. 3
  REST, OpenAPI               :2025-10-29, 3h  <!--LF8-->
 section Do 30.10. 8
  FastAPI, SQLite SQL-Injections     :2025-10-30, 8h  <!--LF8b-->
```

```mermaid
gantt
 title Dezember (13UE LF7 + 23UE LF8 + 2UE PV)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section Mo 01.12. 3
  HTTP, MQTT                  :2025-12-01, 3h
 section Di 02.12. 3
  UART, I2C, SPI              :2025-12-02, 3h
 section Do 04.12. 5
  Wiederholung, Q&A           :2025-12-04, 5h
 section Fr 05.12. 4
  Klassenarbeit               :crit, 2025-12-05, 2h
  LF8 Praxis                  :2025-12-05, 4h
  SOL LF8 Praxis              :crit, 2025-12-05, 2h
 section Mo 08.12. 3
  XML, DTD, SOAP              :2025-12-08, 3h
 section Di 09.12. 3
  JSON, JSON Schema           :2025-12-09, 3h
 section Mi 10.12. 5
  LF8 Praxis                  :2025-12-10, 5h
 section Fr 12.12. 8
  LF8 Praxis                  :2025-12-12, 6h
  SOL PV                      :crit, 2025-12-12, 2h
```

```mermaid
gantt
 title Januar-Februar (31UE LF8 + 18UE PV)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section Mo 12.01. 3
  PV                         :2026-01-12, 3h
 section Di 13.01. 3
  Wiederholung APIs, Datenaustauschformate  :2026-01-13, 3h
 section Mi 14.01. 5
  Wiederholung DB, SQL       :2026-01-14, 5h
 section Do 15.01. 5
  Q&A, Übungsaufgaben        :2026-01-15, 5h
 section Fr 16.01. 8
  Klassenarbeit              :crit, 2026-01-16, 2h
  LF8 ERM + Praxis           :2026-01-16, 4h
  SOL ERM                    :crit, 2026-01-16, 2h
 section Mo 02.02. 5
  LF8 Praxis                 :2026-02-02, 5h
 section Di 03.02. 3
  LF8 Praxis                 :2026-02-03, 1h
  PV                         :2026-02-03, 2h
 section Mi 04.02. 4
  LF8 Projektpräsentation    :2026-02-04, 4h
 section Do 05.02. 5
  PV                         :2026-02-05, 5h
 section Fr 06.02. 8
  PV                         :2026-02-06, 6h
  SOL PV                     :crit, 2026-02-06, 2h
```

```mermaid
gantt
 title März (11UE LF7)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section Do 26.03. 5
  Funktionsweise Prozessor      :2026-03-26, 5h
 section Fr 27.03. 6
  Systemprogrammierung          :2026-03-27, 4h
  SOL Projektplan               :crit, 2026-03-27, 2h
```

```mermaid
gantt
 title Mai-Juni (33UE LF7)
 dateFormat YYYY-MM-DD
 axisFormat %d.%m.
 section Do 21.05. 5
  Vorstellung Praxisprojekte    :crit, 2026-05-21, 2h
  Praxis                        :2026-05-21, 3h
 section Fr 22.05. 6
  Potenzielle Gefahren, Schutzbedarfsanalyse, FMEA  :2026-05-22, 2h
  Praxis                        :2026-05-22, 2h
  SOL Projektdokumentation, Schutzbedarfsanalyse    :crit, 2026-05-22, 2h
 section Di 09.06. 6
  Praxis                        :2026-06-09, 6h
 section Mi 10.06. 5
  Praxis (Benotung)             :crit, 2026-06-10, 5h
 section Do 18.06. 5
  Praxis                        :2026-06-18, 5h
 section Fr 19.06. 6
  Projektpräsentation           :2026-06-19, 4h
  SOL Projektdokumentation      :2026-06-19, 2h
```

## Leistungskontrollen

* Soll Notendichte: 7 
* Minimum Klassenarbeiten (>45min, doppelte Wertung): 2
* Sonstige Noten: >=3

> * **1. Klassenarbeit 05.09.** ~90min (einseitig beschrifteter A4 Notizzettel + 1 einfacher Taschenrechner ohne Binärberechnungen)
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

> * **2. Klassenarbeit 27.03.** (1.+2. UE) ~90min (einseitig beschrifteter A4 Notizzettel)
>   * Auswahl [Hardwareplatformen und Programmiersprachen](./microcontroller/beispiele.md)
>   * [Rechnernetze / Topologien](rechnernetze.md)
>   * [OSI-Modell](osi.md) (insbesondere Physical Layer und anwendungsorientierte Protokolle)
>   * [HTTP](http.md), [MQTT](mqtt.md)
>   * [UART](bituebertragung.md#uart), [SPI](rechnernetze.md#spi), [I²C](rechnernetze.md#i²c)
>   * Grundlagen Programmierung (Variablen, While, If/Else, Funktionen)
>     * Siehe Programmierbeispiele [Pi](pi.md), [I²C-Beispiel (main.py)](rechnernetze.md#i²c)

Programmier-Übungsaufgaben:
* Blink [Pi Pico](https://wokwi.com/projects/300504213470839309), [ESP32](https://wokwi.com/projects/359801682833812481)
* [Ampel](https://wokwi.com/projects/432915684639002625)
* [Buzzer](https://wokwi.com/projects/432915379839949825)
* [Button](https://wokwi.com/projects/432915323107785729)
* [7-Segment + Schalter](https://wokwi.com/projects/300210834979684872)

> * **Mündliche Note 21.05.**
>   * Vorstellung Projektplan (SOL vom 27.03.)
>   * Bisherige Mitarbeit

> * **Bewertung Praxisprojekt** am **10.06.**
>   * **Note für fachliche Leistung**
>   * **Note für Mitarbeit**
> * Projektpräsentation 19.06. (nach Notenschluss)
