# Binärzahlen

Computer kennen nur 1 und 0 und arbeiten mit [Binärzahlen (im Dualsystem)](https://de.wikipedia.org/wiki/Dualsystem).

> Wieviele Zustände können mit einer gegebenen Anzahl von [Bits](https://de.wikipedia.org/wiki/Dualsystem#Berechnung_ben%C3%B6tigter_Stellen) dargestellt werden?

## Umrechnung

* [Dual nach Dezimal](https://de.wikipedia.org/wiki/Dualsystem#Vom_Dualsystem_ins_Dezimalsystem)

Beispiel:

> 100110
>
> = 1*32 + 0*16 + 0*8 + 1*4 + 1*2 + 0*1
>
> = 32 + 0 + 0 + 4 + 2 + 0
>
> = 38

* [Dezimal nach Dual](https://de.wikipedia.org/wiki/Dualsystem#Vom_Dezimalsystem_ins_Dualsystem)

Beispiel:

> 116
>
> 116 < 128
> 
> ---> 0
> 
> 116 >= 64 ---> 116 - 64 = 52
> 
> ---> 1
>
> 52 >= 32 ---> 52 - 32 = 20
>
> ---> 1
> 
> 20 >= 16 ---> 20 - 16 = 4
>
> ---> 1
>
> 4 < 8
>
> ---> 0
>
> 4 >= 4 ---> 4 - 4 = 0
>
> ---> 1
>
> 0 < 2
>
> ---> 0
>
> 0 < 1
>
> ---> 0
>
> * von oben nach unten die einzelnen 0 und 1 lesen
> * Lösung: 01110100

Beispiel mit anderem Lösungsweg:

> 116
>
> 116 / 2 = 58, Rest 0
>
> ---> 0
>
> 58 / 2 = 29, Rest 0
>
> ---> 0
> 
> 29 / 2 = 14, Rest 1
>
> ---> 1
>
> 14 / 2 = 7, Rest 0
>
> ---> 0
>
> 7 / 2 = 3, Rest 1
>
> ---> 1
>
> 3 / 2 = 1, Rest 1
>
> ---> 1
>
> 1 / 2 = 0, Rest 1
>
> ---> 1
>
> * ! Achtung: von unten nach oben die einzelnen 0 und 1 lesen
> * Lösung: 1110100

## [Addition](https://de.wikipedia.org/wiki/Dualsystem#Grundrechenarten_im_Dualsystem)

## [Integer overflow](https://de.wikipedia.org/wiki/Arithmetischer_%C3%9Cberlauf)
