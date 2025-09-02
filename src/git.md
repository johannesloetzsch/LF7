# Git

<!--
## Einordnung

> Vergleich von SCMs mit Backups und Dateisystem-Snapshots


### Arten von SCMs (**Source Code Management**)

#### Zentral

* \*~
* `diff` + `patch`

* CVS (Concurrent Versions System)
* SVN (Subversion)

#### Dezentral

* Bazaar
* Mercurial (hg)
* **Git**
-->

## Praxis

* [Download von Git](https://git-scm.com/)
* [OhMyGit — spielerisch Git lernen](https://ohmygit.org/)


## Beispiel
Die aus meiner Sicht für Anfänger wichtigsten Operation:

<!--
siehe [git-Subcommands](https://johannesloetzsch.github.io/linux-praktikum/versionskontrolle.html)
-->

```bash
## Eine Kopie eines existierenden Repositories klonen und in das Verzeichnis wechseln
git clone https://github.com/johannesloetzsch/LF10b.git
cd LF10b/

## Eine Datei editieren, die Änderungen betrachten und rückgängig machen
nano src/versionierung.md 
git status
git diff
git restore src/versionierung.md

## Eine Datei editieren, die Änderungen betrachten…
nano src/versionierung.md  ## man könnte auch vim benutzen
git status
git diff
## Die geänderte Datei für den nächsten Commit einplanen
git add src/versionierung.md 
git status 
## Einen neuen Commit erstellen
git commit

## Die Commit-Historie anschauen
git log
```

```bash
## Ein neues Git-Repository anlegen und in das Verzeichnis wechseln
git init myproject
cd myproject/
```


## SOL

```
Erarbeiten Sie sich die Grundlagen zu Git.

Von folgenden Subcommands sollten Sie wissen, was sie tun:


git init

git clone

git status

git add

git diff

git commit

git restore




Empfehlung: Wenn Git für sie komplett neu ist, probieren sie zum lernen gerne die ersten Level von https://ohmygit.org/




Abgabe: Als Ergebnis wird erwartet, dass Sie zwischen folgenden beiden Aufgaben auswählen:




Variante 1:

a) erstellen Sie per "git init" ein neues git Repository

b) legen Sie die Dateien aus ihrem Arduino-Projekt in dem Repository ab

c) wählen Sie die Daten zum commit aus ("git add") und erstellen Sie einen commit

d) ändern Sie Dateien oder fügen Sie neue Dateien (z.B. eine README.md) hinzu

e) erstellen Sie einen zweiten commit mit den Änderungen

f) versuchen Sie Ihr git Repository auf einen Git-Server (z.B. https://github.com oder https://gitlab.com) hochzuladen. Wenn Sie erfolgreich sind, reicht als Abgabe ein Link

g) falls Sie mit f) nicht erfolgreich waren, erzeugen Sie ein zip-Archiv des Repositories und laden Sie dieses als Abgabe hoch

 

Variante 2:

a) erstellen Sie einen Github-Account (wenn Sie noch keinen haben)

b) forken Sie mein repository https://github.com/johannesloetzsch/LF7

c) clonen Sie ihren Fork auf ihren Computer

d) editieren Sie mindestens eine Datei (beheben Sie z.B. einen Tipp-/Rechtschreibfehler oder fügen sie zu einem Thema ergänzende Informationen wie einen nützlichen Link oder den Vorschlag einer Definition eines Begriffes hinzu)

e) commiten und pushen Sie die Änderungen

f) stellen Sie mir einen Pull-Request (das reicht als Abgabe)
```


**Zusatzaufgabe** für Schüler, die sich bereits mit Git auskennen:

Frischen Sie ihr Wissen zu [DevOps](./devops.md) auf. 


<!--
SOL - Definition Musterlösung

```
git init - Initialisiert ein neues lokales und leeres Git-Repository.

git clone - Klont ein Repository in ein neues Verzeichnis. Dieses muss/wird mit der URL des Repositorys angegeben.

git status - Zeigt den Status des Arbeitsverzeichnisses und des Staging-Bereichs an. Es zeigt an, welche Dateien geändert wurden, welche Dateien zum Staging-Bereich hinzugefügt wurden und welche Dateien im Staging-Bereich sind.

git add - Fügt Dateien zum Staging-Bereich hinzu. Es gibt verschiedene Möglichkeiten, Dateien hinzuzufügen.

git diff - Zeigt die Unterschiede zwischen zwei Commits, zwischen einem Commit und dem Arbeitsverzeichnis oder zwischen zwei Branches an.

git commit - Erstellt einen neuen Commit. Dieser Commit ist nur lokal verfügbar und muss mit git push auf den Remote-Server hochgeladen werden.

git restore - Stellt Dateien aus dem Staging-Bereich oder dem letzten Commit wieder her.
```
-->
