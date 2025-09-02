# [Widerstände](https://de.wikipedia.org/wiki/Elektrischer_Widerstand)

<!-- toc -->


Schaltzeichen: ![](https://upload.wikimedia.org/wikipedia/commons/c/c3/Resistor_symbol_IEC.svg)

![](https://upload.wikimedia.org/wikipedia/commons/e/e3/3_Resistors.jpg)

=> [Farbkodierung](https://de.wikipedia.org/wiki/Widerstand_(Bauelement)#Farbkodierung_auf_Widerst%C3%A4nden)

### Berechnung

`R = U / I`

Einheit: `Ω = V / A`

### Messung

=> mittels [Ohmmeter](https://de.wikipedia.org/wiki/Widerstandsmessger%C3%A4t)

![](https://upload.wikimedia.org/wikipedia/commons/5/59/AMM_Skalen_nl.jpg)

## [Vorwiderstände](https://de.wikipedia.org/wiki/Vorwiderstand)

=> zur Strombegrenzung

![](https://upload.wikimedia.org/wikipedia/commons/9/9a/Vorwiderstand.png)

`U`<sub>V</sub>` = U - U`<sub>R</sub>

`R`<sub>V</sub>` = U`<sub>V</sub>` / I`

> gegeben:
>
> **U** => Spannungsversorgung
>
> **U<sub>R</sub>** => Spannung, die über zu schützendem Bauteil (z.B. LED) abfallen soll
>
> **I** => Strom, der maximal durch das zu schützende Bauteil fließen soll
>
> gesucht:
>
> **R<sub>V</sub>** => benötigter Vorwiederstand

> Welchen Wiederstand wählen wir aus, wenn ein Wiederstand benötigter größe nicht vorhanden ist?

## [Pull-up und Pull-down](https://de.wikipedia.org/wiki/Open_circuit#Pull-down)

=> zieht Signalleitung standartmäßig auf gewünschten [Pegel](https://de.wikipedia.org/wiki/Logikpegel#Standardwerte)

Erklärung:

* **Schalter geöffnet:** Dem Strom bleibt nur die Leitung über den Pull-Up/Down-Widerstand. Somit liegt an der Signalleitung der standardmäßig gewünschte Pegel an.

* **Schalter geschlossen:** Es gibt zwei Leitungen über die Strom fließen kann: Den großen Pull-Up/Down-Widerstand und (nahezu) widerstandslosen Leiter mit Schalter. Da der Strom den Weg des geringsten Widerstands nimmt, fließt dieser über den geschlossenen Schalter. Somit liegt an der Signalleitung der am Schalter anliegende Pegel an.

![](https://upload.wikimedia.org/wikipedia/commons/4/4e/Pull-down-Widerstand_mit_Taster.svg)


## Praxis
=> Grundschaltungen ausprobieren

* [ ] Schaltkreis mit LED + Vorwiderstand
  * [ ] Taster einbauen
* [ ] AND und OR mit 2 Tastern
* [ ] NOT mit Taster und Pull-up-Wiederstand
  * [ ] 2 verschiedenfarbige LEDs am Ein-/Ausgang
* [ ] XOR mit 2 „Umschaltern“ bzw. [Jumper wires](https://en.wikipedia.org/wiki/Jump_wire)
* [ ] AND, OR, NOT mit Transistoren

Zusatzaufgaben:
* [ ] [XOR und Halbaddieren mit 7 Transistoren](https://www.leisering.net/4bit_va/inhaltsverzeichnis.html#kap06)
* [ ] Volladdierer

### Benötigstes Material pro Gruppe

* [ ] Spannungsversorgung
  * 5V von Raspberry-Pi + USB-Netzteil => [Pinout](pi.md)
  * [ ] je ein Jumper Wire `female->male` (rot+schwarz)
* [ ] Breadboard + Jumper Wires `male->male` (verschiedenfarbig)
* [ ] 2 LEDS (verschiedenfarbig) + 2 Vorwiederstände (330Ω)
* [ ] 2 Taster
* [ ] 1 Pull-Up- bzw. Pull-Down-Widerstand (470Ω-1kΩ)
* [ ] 2 Transistoren mit 10kΩ Basis-Widerstand


### Breadboard
<img src="https://upload.wikimedia.org/wikipedia/commons/e/e8/Breadboard.png" style="transform: rotate(90deg);  margin: 100px"/>
