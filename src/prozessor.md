# Prozessoren

> SOL „Funktionsweise von Prozessoren“
>
> Erkundigen Sie sich selbstständig darüber, wie es möglich ist, mittels Maschinen zu rechnen.
> Als Einstieg wird folgendes Video empfohlen: [A Computer Built With Dominos](https://www.youtube.com/watch?v=w6E7aQnA4Ws).
>
> Beantworten Sie die folgenden Fragen:
>
> 1. Wie funktioniert das Binärsystem?
> 2. Schreiben Sie die Zahlen 0-7 als Binärzahl auf.
> 3. Benennen Sie 4 verschiedene zweistellige logische Verknüpfungen (Logikgatter).
> 4. Was ist ein Halbaddierer?
> 5. Wieviele Eingänge und wieviele Ausgänge hat ein Halbaddierer?
> 6. Zeichnen oder beschreiben Sie eine Schaltung, wie ein Halbaddierer aus einfachen Logikgattern aufgebaut werden kann.
> 7. Finden Sie Möglichkeiten, wie Logikgatter mittels Murmeln, Wasser oder in Minecraft aufgebaut werden können?


## [Transistoren](https://de.wikipedia.org/wiki/Bipolartransistor)

![npn](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Diagrama_de_Transistor_NPN.svg/220px-Diagrama_de_Transistor_NPN.svg.png)

![npn](https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/NPN_BJT_-_Structure_%26_circuit.svg/500px-NPN_BJT_-_Structure_%26_circuit.svg.png)

[Aufbau von Gattern und Addierer mit BJT-Transistioren](https://www.leisering.net/4bit_va/inhaltsverzeichnis.html#anhb)

<iframe width="560" height="315" src="https://www.youtube.com/embed/B2482h_TNwg?si=AJIQBoJ1pH0L5520" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<!-- https://github.com/SebLague/Digital-Logic-Sim -->


## [Von-Neumann-Zyklus](https://de.wikipedia.org/wiki/Von-Neumann-Zyklus)

[![cpu](https://upload.wikimedia.org/wikipedia/commons/2/2c/Proz1-d.png)](https://de.wikipedia.org/wiki/Prozessor#Verarbeitung_eines_einzelnen_Befehls)

1. `FETCH` (Befehlsabruf):
    * Nächsten Befehl (entsprechend Adresse im Befehlszähler) aus Arbeitsspeicher in das Befehlsregister laden und Befehlszähler inkrementieren
2. `DECODE`(Dekodierung):
    * Der Befehl wird durch das Steuerwerk in Schaltinstruktionen für das Rechenwerk aufgelöst
3. `FETCH OPERANDS`(Operandenabruf):
    * Operanden werden aus dem Speicher laden
4. `EXECUTE` (Befehlsausführung):
    * Arithmetische oder logische Operation wird vom Rechenwerk berechnet. *(Bei Sprungbefehlen und erfüllter Sprungbedingung wird der Befehlszähler angepasst)*
5. `WRITE BACK` (Rückschreiben des Resultats): Ergebnis der Berechnung wird in den Speicher zurückgeschrieben *(falls nötig)*

## Assembler
[ARM instruction summary](https://developer.arm.com/documentation/dui0489/i/arm-and-thumb-instructions/arm-and-thumb-instruction-summary)

Beispiel ([blinky-rust](https://github.com/johannesloetzsch/blinky-rust-nix/blob/65c330307cd16a7519603acc304f5239a195b485/src/main.rs#L14)):

```sh
git clone git@github.com:johannesloetzsch/blinky-rust-nix.git -b asm
cd blinky-rust-nix; nix develop
cargo rustc -- --emit asm
grep -m1 main_loop: -A43 target/thumbv7m-none-eabi/debug/deps/blinky_rust-*.s | bat --file-name example.s
```

```asm
.LBB26_1:
    .loc    11 0 5 is_stmt 0
    subs    r0, r7, #1
    .loc    11 15 9 is_stmt 1
    str r0, [sp]
    bl  _ZN136_$LT$stm32f1xx_hal..gpio..gpioc..PC13$LT$stm32f1xx_hal..gpio..Output$LT$MODE$GT$$GT$$u20$as$u20$embedded_hal..digital..v2..OutputPin$GT$8set_high17h41a8f7d2c1b1fab3E
    bl  _ZN4core6result19Result$LT$T$C$E$GT$2ok17hbba81ef68e509503E
    .loc    11 16 9
    ldr r0, [sp, #8]
    mov.w   r1, #1000
    str r1, [sp, #4]
    bl  _ZN97_$LT$stm32f1xx_hal..delay..Delay$u20$as$u20$embedded_hal..blocking..delay..DelayMs$LT$u16$GT$$GT$8delay_ms17h9fb44941d1d2b02bE
    ldr r0, [sp]
    .loc    11 18 9
    bl  _ZN136_$LT$stm32f1xx_hal..gpio..gpioc..PC13$LT$stm32f1xx_hal..gpio..Output$LT$MODE$GT$$GT$$u20$as$u20$embedded_hal..digital..v2..OutputPin$GT$7set_low17h5e48a13c9b6d1e70E
    bl  _ZN4core6result19Result$LT$T$C$E$GT$2ok17hbba81ef68e509503E
    ldr r1, [sp, #4]
    .loc    11 19 9
    ldr r0, [sp, #8]
    bl  _ZN97_$LT$stm32f1xx_hal..delay..Delay$u20$as$u20$embedded_hal..blocking..delay..DelayMs$LT$u16$GT$$GT$8delay_ms17h9fb44941d1d2b02bE
    b   .LBB26_1
```

### Binary

```sh
## laut disassembly startet <main_loop> bei 0800_016c, das ist im ELF-binary an 1_016c
hexdump -s $((16#1016c)) target/thumbv7m-none-eabi/debug/deps/blinky_rust-* |head -n4
```

```hexdump
001016c b580 466f b084 9002 e7ff 1e78 9000 f000
001017c f92f f000 f886 9802 f44f 717a 9101 f000
001018c fc30 9800 f000 f917 f000 f87b 9901 9802
001019c f000 fc27 e7e9 b580 466f f000 f800 b580
```

```sh
## …und an adresse 717a befindet sich #0x3e8, also #1000
hexdump -s $((16#20717a)) target/thumbv7m-none-eabi/debug/deps/blinky_rust-* |head -n 1
```

```hexdump
020717a 4202 070d 0000 0018 0000 03e8 0000 0000
```

### Disassemble

```sh
cargo objdump -- -S target/thumbv7m-none-eabi/debug/deps/blinky_rust-* | grep -m1 '<main_loop>' -A 26
```

```asm
0800016c <main_loop>:
; fn main_loop(mut led: PC13<Output<PushPull>>, mut delay: Delay) -> ! {
 800016c: b580         	push	{r7, lr}
 800016e: 466f         	mov	r7, sp
 8000170: b084         	sub	sp, #0x10
 8000172: 9002         	str	r0, [sp, #0x8]
;     loop {
 8000174: e7ff         	b	0x8000176 <main_loop+0xa> @ imm = #-0x2
 8000176: 1e78         	subs	r0, r7, #0x1
;         led.set_high().ok();
 8000178: 9000         	str	r0, [sp]
 800017a: f000 f92f    	bl	0x80003dc <_ZN136_$LT$stm32f1xx_hal..gpio..gpioc..PC13$LT$stm32f1xx_hal..gpio..Output$LT$MODE$GT$$GT$$u20$as$u20$embedded_hal..digital..v2..OutputPin$GT$8set_high17h41a8f7d2c1b1fab3E> @ imm = #0x25e
 800017e: f000 f886    	bl	0x800028e <_ZN4core6result19Result$LT$T$C$E$GT$2ok17hbba81ef68e509503E> @ imm = #0x10c
;         delay.delay_ms(1000_u16);
 8000182: 9802         	ldr	r0, [sp, #0x8]
 8000184: f44f 717a    	mov.w	r1, #0x3e8
 8000188: 9101         	str	r1, [sp, #0x4]
 800018a: f000 fc30    	bl	0x80009ee <<stm32f1xx_hal::delay::Delay as embedded_hal::blocking::delay::DelayMs<u16>>::delay_ms::h9fb44941d1d2b02b> @ imm = #0x860
 800018e: 9800         	ldr	r0, [sp]
;         led.set_low().ok();
 8000190: f000 f917    	bl	0x80003c2 <_ZN136_$LT$stm32f1xx_hal..gpio..gpioc..PC13$LT$stm32f1xx_hal..gpio..Output$LT$MODE$GT$$GT$$u20$as$u20$embedded_hal..digital..v2..OutputPin$GT$7set_low17h5e48a13c9b6d1e70E> @ imm = #0x22e
 8000194: f000 f87b    	bl	0x800028e <_ZN4core6result19Result$LT$T$C$E$GT$2ok17hbba81ef68e509503E> @ imm = #0xf6
 8000198: 9901         	ldr	r1, [sp, #0x4]
;         delay.delay_ms(1000_u16);
 800019a: 9802         	ldr	r0, [sp, #0x8]
 800019c: f000 fc27    	bl	0x80009ee <<stm32f1xx_hal::delay::Delay as embedded_hal::blocking::delay::DelayMs<u16>>::delay_ms::h9fb44941d1d2b02b> @ imm = #0x84e
 80001a0: e7e9         	b	0x8000176 <main_loop+0xa> @ imm = #-0x2e
```

## [bare-metal-programming](https://github.com/cpq/bare-metal-programming-guide)
