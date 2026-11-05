# [MQTT](https://de.wikipedia.org/wiki/MQTT)
**M**essage **Q**ueuing **T**elemetry **T**ransport

* Publish/Subscribe

* Clients („**Subscriber**“) können ein „Topic“ abonnieren
  * TCP-Verbindung wird offen gehalten
  * Server („**Broker**“) kann Clients über bestehende Verbindung über Updates informieren\
  (sobald Broker Nachrichten von einem „**Publisher**“ erhält)

* Üblicherweise über **TCP**
  * **1883** mqtt://
  * 8883 mqtts://
  * auch über Websockets oder UDP („MQTT-SN“ für Sensornetzwerke) möglich

```mermaid
flowchart LR
    P1[Publisher 1] --> B[Broker]
    P2[Publisher 2] --> B
    P3[Publisher 3] --> B
    P4[Publisher 4] --> B
    P5[Publisher 5] --> B
    B --> S1[Subscriber 1]
    B --> S2[Subscriber 2]
    B --> S3[Subscriber 3]
    B --> S4[Subscriber 4]
    B --> S5[Subscriber 5]
```

## Sequenzdiagramm

```mermaid
sequenceDiagram
    participant P as Publisher
    participant B as Broker
    participant S as Subscriber

    S-->>B: TCP SYN (Port 1883)
    B-->>S: TCP SYN-ACK
    S-->>B: TCP ACK
    S->>B: SUBSCRIBE (Topic fi/buttonGPIO2)
    P-->>B: TCP SYN (Port 1883)
    B-->>P: TCP SYN-ACK
    P-->>B: TCP ACK
    P->>B: PUBLISH (Topic fi/buttonGPIO2, Payload "1")
    B->>S: PUBLISH wird weitergeleitet
```

## Vergleich mit HTTP

|                   | HTTP                    | MQTT                                           |
| ----------------- | ----------------------- | ---------------------------------------------- |
| Typische Nutzung  | **Web, API**            | **IoT/M2M**, Sensorik, instabile Netze         |
| Muster            | Request-Response        | Publish/Subscribe                              |
| Kopplung          | Client kennt Server     | Publisher/Subscriber durch Broker entkoppelt   |
| Richtung          | durch Client initiiert  | Broker kann an Subscriber pushen               |
| Overhead          | textuelle Header        | winziger Binärheader (~2 Byte)                 |
| Zustand           | zustandslos             | Broker merkt sich Sessions & Retained Messages |

## Demo

> **💻** Broker starten, Subscriben, Publishen
>
> ```bash
> mosquitto  ## startet den broker [1]
> mosquitto_sub -h 127.0.0.1 -p 1883 -u fi -P geheim -t fi/buttonGPIO2
> mosquitto_pub -h 127.0.0.1 -p 1883 -u fi -P geheim -t fi/buttonGPIO2 -m '1'
> ```

> [1] **⚠️** Bitte [**Firewall**](https://johannesloetzsch.github.io/LF11b/netzwerk/firewalls.html) (Paketfilter/SPI) nutzen ;)
>
> → [Anleitung für Windows](https://support.microsoft.com/de-de/windows/security/windows-security/firewall-and-network-protection-in-the-windows-security-app) \
> → [GUI-Beispiel für Linux](https://github.com/costales/gufw)

> **💬❓** Welche Sicherheitslücke hätte obriges Setup, wenn sie es produktiv in Ihrem Netz einsetzen würden?

## Prüfungsaufgabe

> **📝❗** FiSi AP2 Analyse Sommer 2025 Aufgabe 4c
