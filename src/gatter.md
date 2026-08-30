# [Logikgatter](https://de.wikipedia.org/wiki/Logikgatter)

<!-- toc -->

> Aufgabe 6 von Seite 78 aus „Prüfungsvorbereitung Aktuell Teil 1“ (Europa Verlag)


## [NOT](https://de.wikipedia.org/wiki/Nicht-Gatter)

`Y = NOT X = ¬ X = X̅`

| X | NOT X |
| - | ----- |
| 0 | 1     |
| 1 | 0     | 

<img src="https://upload.wikimedia.org/wikipedia/commons/3/31/IEC_NOT_label.svg" style="width: 30%" /><br/>

<img src="https://upload.wikimedia.org/wikipedia/commons/a/a6/Not.PNG" style="width: 60%" />

<img src="https://upload.wikimedia.org/wikipedia/commons/a/a0/Simplified_NOT_gate_circuit_using_transistor.svg" style="width: 60%" />

## [AND](https://de.wikipedia.org/wiki/Und-Gatter)

`Y = X1 AND X2 = X1 & X2 = X1 ∧ X2 = X1 • X2 = X1 X2`

| X1 | X2 | X1 AND X2 |
| -- | -- | --------- |
| 0  | 0  | 0         |
| 0  | 1  | 0         |
| 1  | 0  | 0         |
| 1  | 1  | 1         |

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/IEC_AND_label.svg" style="width: 30%" /><br/>

<img src="https://upload.wikimedia.org/wikipedia/commons/9/94/AND-Gatter.svg" style="width: 60%" />

<img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/TransistorANDgate.png" style="width: 60%" />

## [OR](https://de.wikipedia.org/wiki/Oder-Gatter)

`Y = X1 OR X2 = X1 ∨ X2 = X1 + X2`

| X1 | X2 | X1 OR X2 |
| -- | -- | -------- |
| 0  | 0  | 0        |
| 0  | 1  | 1        |
| 1  | 0  | 1        |
| 1  | 1  | 1        |

<img src="https://upload.wikimedia.org/wikipedia/commons/4/40/IEC_OR_label.svg" style="width: 30%" /><br/>

<img src="https://upload.wikimedia.org/wikipedia/commons/5/51/OR-Gatter.png" style="width: 60%" />

<img src="https://upload.wikimedia.org/wikipedia/commons/0/01/Transistor_OR_Gate.png" style="width: 60%" />

## [XOR](https://de.wikipedia.org/wiki/Exklusiv-Oder-Gatter)

`Y = X1 XOR X2 = X1 ⊕ X2`

| X1 | X2 | X1 XOR X2 |
| -- | -- | --------- |
| 0  | 0  | 0         |
| 0  | 1  | 1         |
| 1  | 0  | 1         |
| 1  | 1  | 0         |

<img src="https://upload.wikimedia.org/wikipedia/commons/6/6c/IEC_XOR_label.svg" style="width: 30%" /><br/>

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Logic-XOR.svg" style="width: 60%" />

<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/XOR_Aufbau_Und-Oder.svg" style="width: 60%" />

<img src="https://www.leisering.net/4bit_va/xor_gatter.gif" style="width: 60%">

## [Halbaddierer](https://de.wikipedia.org/wiki/Halbaddierer)

| X1 | X2 | Übertrag c | Summe s |
| -- | -- | ---------- | ------- |
| 0  | 0  |	0          | 0       |
| 0  | 1  | 0          | 1       | 
| 1  | 0  | 0          | 1       |
| 1  | 1  | 1          | 0       |

<img src="https://upload.wikimedia.org/wikipedia/commons/1/15/Halbaddierer_Aufbau.svg" style="width: 60%" />

## [Volladdierer](https://de.wikipedia.org/wiki/Volladdierer)

| X1 | X2 | Cin | Cout | s |
| -- | -- | --- | ---- | - |
| 0  | 0  | 0   | 0    | 0 |
| 0  | 0  |	1   | 0    | 1 |
| 0  | 1  |	0   | 0    | 1 |
| 0  | 1  |	1   | 1    | 0 |
| 1  | 0  |	0   | 0    | 1 |
| 1  | 0  |	1   | 1    | 0 |
| 1  | 1  |	0   | 1    | 0 |
| 1  | 1  |	1   | 1    | 1 |

<img src="https://upload.wikimedia.org/wikipedia/commons/6/6c/Volladdierer_Aufbau_DIN40900.svg" style="width: 60%" />

## Praxis

[Schaltungen](https://www.leisering.net/4bit_va/inhaltsverzeichnis.html#anhb) für Aufbau von Gattern und Addierer mit npn-BJT-Transistioren



## Übungen

Logikgatter aufbauen und verstehen anhand [nandgame.com](https://nandgame.com/) 
