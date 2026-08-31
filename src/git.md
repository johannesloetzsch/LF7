# Git

> 💬❓ Was ist Git?
> * Wofür wird es benötigt?
> * Wie verwendet man es?

<!-- toc -->

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

## Welche Befehle sollte ich kennen?
### 2. Lehrjahr

```
git init

git clone

git status

git diff

git add

git commit

git log

git reset
```

### 3. Lehrjahr

```
git branch

git checkout

git merge

git remote

git fetch

git pull

git push
```

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


## Lernmaterial und Praxis

* Offizielle [Lehrmaterialien](https://git-scm.com/learn) und [Reference](https://git-scm.com/docs)
* [Kurze Einfuhrung in Git](./git_nico.md)
* [OhMyGit — spielerisch Git lernen](https://ohmygit.org/)
* [Download von Git](https://git-scm.com/)


## SOL

```
Erarbeiten Sie sich die Grundlagen zu Git.

Empfehlung: Wenn Git für sie komplett neu ist, probieren sie zum lernen gerne die ersten Level von https://ohmygit.org/


Abgabe:

a) erstellen Sie per "git init" ein neues git Repository

b) legen Sie die Sourcecode des von Ihnen implementieren Sortierverfahrens in dem Repository ab

c) wählen Sie die Daten zum commit aus ("git add") und erstellen Sie einen commit

d) ändern Sie Dateien oder fügen Sie neue Dateien (z.B. eine README.md) hinzu

e) erstellen Sie einen zweiten commit mit den Änderungen

f) versuchen Sie Ihr git Repository auf einen Git-Server (z.B. https://codeberg.org, https://gitlab.com, https://github.com, …) hochzuladen. Wenn Sie erfolgreich sind, reicht als Abgabe ein Link (auf ein öffentliches Repository)

g) falls Sie mit f) nicht erfolgreich waren, erzeugen Sie ein zip-Archiv des Repositories und laden Sie dieses als Abgabe hoch
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
