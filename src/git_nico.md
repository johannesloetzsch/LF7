<!-- danke @nico / https://schulstick.org -->

# Zusammenfassung Git

## Was ist Git?
Git ist ein Programm, das dir hilft, den Überblick über Dateien in einem Projekt zu behalten. Es speichert
Änderungen, die du an deinen Projekten machst, und ermöglicht es dir, ältere Versionen wiederherzustellen.
So kannst du jederzeit zu einer früheren, festgehaltenen Version zurückkehren. Git bietet viele Vorteile: Es
erleichtert die Teamarbeit, da mehrere Personen gleichzeitig an einem Projekt arbeiten können. Außerdem sorgt
es für mehr Organisation, da du genau sehen kannst, wer welche Änderungen vorgenommen hat und wann diese passiert sind.

Mit Git kannst du Änderungen festhalten, indem du deine Arbeit speicherst, was als "committen" bezeichnet wird.
Du kannst auch verschiedene Versionen miteinander vergleichen, um genau zu erkennen, was sich geändert hat.
Darüber hinaus unterstützt Git in Verbindung mit einem Server die Zusammenarbeit, indem es dir ermöglicht,
Dateien mit anderen zu teilen und Änderungen miteinander zu kombinieren.

Git wurde 2005 von Linus Torvalds, dem Schöpfer des Linux-Kernels, entwickelt, um die Versionsverwaltung für
große Softwareprojekte zu verbessern. Es entstand als Antwort auf die Notwendigkeit eines schnellen,
verlässlichen und verteilten Systems zur Zusammenarbeit in Entwicklerteams.

## Grundlegende Konzepte
Git basiert auf einigen grundlegenden Konzepten, die wichtig sind, um es effektiv zu nutzen. Das Herzstück
eines Git-Projekts ist das Repository. Ein Repository ist wie ein Ordner, der nicht nur deine Dateien enthält,
sondern auch alle Änderungen, die du daran vornimmst. Du kannst ein neues Repository erstellen, indem du den
Befehl `git init` in deinem Projektordner ausführst. Dadurch wird Git in diesem Ordner aktiviert und bereitgestellt,
um Änderungen zu verfolgen.

Sobald du eine Änderung an deinen Dateien vorgenommen hast, kannst du diese mit dem Befehl `git add` zur sogenannten
Staging-Area hinzufügen. Hier sammelst du Änderungen, die du in einem Schritt speichern möchtest. Mit `git commit`
werden diese Änderungen dann endgültig festgehalten und in die Historie aufgenommen. Ein Commit speichert also
einen "Stand" deines Projekts, der später wiederhergestellt werden kann.

Möchtest du wissen wie der aktuelle Stand der erstellten Daten ist, kannst du `git status` verwenden.

Um Änderungen nachzuvollziehen, bietet Git verschiedene Befehle. Mit `git show` kannst du dir die Details eines
bestimmten Commits ansehen, z. B. welche Dateien geändert wurden. Der Befehl `git diff` zeigt dir die Unterschiede
zwischen zwei Versionen deiner Dateien. Um den gesamten Verlauf deiner Änderungen zu sehen, kannst du `git log`
verwenden, das dir alle Commits in einer chronologischen Liste anzeigt.

## Branches
Ein Branch (zu Deutsch: Zweig) ist wie ein separater Arbeitsbereich innerhalb eines Projekts. Stell dir vor, du arbeitest
an einem neuen Feature oder möchtest etwas ausprobieren, ohne die Hauptversion deines Projekts zu verändern. Mit einem
Branch kannst du diese Änderungen vornehmen, ohne die Hauptversion (oft "main" oder "master" genannt) zu beeinflussen.
Sobald du zufrieden bist, kannst du die Änderungen wieder mit der Hauptversion zusammenführen.

Branches ermöglichen es, parallel zu arbeiten - sei es allein oder im Team. So kannst du sicher experimentieren, Fehler
beheben oder neue Features entwickeln, ohne das Risiko einzugehen, den Hauptcode zu beschädigen.

Du kannst einen neuen Branch erstellen und direkt in diesen wechseln, indem du den folgenden Befehl benutzt: `git checkout -b <name>`.

Wenn du mit deinem Branch fertig bist und die Änderungen in die Hauptversion (oder einen anderen Branch) übernehmen möchtest,
kannst du die Branches zusammenführen - das nennt man "Mergen". Dafür wechselst du zunächst in den Zielbranch (z. B. main) mit:
`git checkout main`

Danach führst du die Änderungen aus deinem Arbeitsbranch mit dem Befehl `git merge <name>` zusammen.

Git kombiniert die Änderungen beider Branches. Falls es keine Konflikte gibt, wird der Merge automatisch abgeschlossen.

## Mergekonflikte
### Warum treten Konflikte auf?
Konflikte in Git entstehen, wenn Git nicht automatisch entscheiden kann, wie Änderungen von verschiedenen Branches kombiniert
werden sollen. Das passiert typischerweise, wenn:
- Zwei Branches dieselbe Stelle in einer Datei verändert haben.
- Eine Änderung in einem Branch eine Datei löscht, die im anderen Branch geändert wurde.
- Änderungen aus unterschiedlichen Branches logisch nicht zusammenpassen.
Git markiert diese Konflikte und fordert dich auf, sie manuell zu lösen. Danach kannst du die Änderungen zusammenführen.

### Konflikte manuell lösen
Wenn ein Konflikt auftritt, zeigt Git betroffene Dateien im Statusbericht an. Die Datei enthält Markierungen, die die
widersprüchlichen Änderungen anzeigen. Du löst den Konflikt, indem du die Markierungen entfernst und die Datei so bearbeitest,
dass sie die gewünschte Version enthält. Das sieht z.B. so aus:
```
<<<<<<< HEAD
Text aus dem main-Branch
=======
Text aus dem feature-branch
>>>>>>> feature-branch
```

## Remote Repositories zur Zusammenarbeit
Für die Zusammenarbeit von mehreren Personen benötigt man einen Git Server. Prinzipiell kann jede Installation von Git
als Server fungieren, solange alle Nutzer diese erreichen können. Häufig werden Platformen wie GitHub, GitLab oder Gitea
verwenden, die weitere Funktionen wie Issue-Tracking und automatisierungen (z. B. continuous integration) bieten.

Um nun das lokale Repository mit dem entfernten Repository zu syncronisieren werden verschiedene Befehle benötigt.

Zunächst wird das entfernte Repository mit `git remote add origin <URL>` unter dem Namen `origin` hinzugefügt.

Mit dem Befehl `git push` kannst du deine lokalen Commits an das entfernte Repository senden. Mit `git pull` holst du
dir die neuesten Änderungen vom entfernten Repository in dein lokales Repository. Diese beiden Befehle reichen aus,
damit zwei Personen gemeinsam an einem Repository arbeiten können.

Falls ihr aber gleichzeitig arbeitet oder vergesst, vor neuen Commits ein `git pull` zu machen, fehlen euch die
neuesten Änderungen aus dem entfernten Repository in eurer lokalen Version. Wenn dein lokales Repository schon neuere
Commits enthält und du es trotzdem mit dem Stand des entfernten Repositorys abgleichen willst, kannst du mit `git fetch`
die Änderungen holen und dann mit `git rebase origin/branch-name` in deine lokale History einfügen.

## Stash
Mit Stashing kannst du Änderungen, die du noch nicht committen möchtest, vorübergehend speichern. So kannst du problemlos
an einer anderen Aufgabe weiterarbeiten, ohne deine aktuellen Änderungen zu verlieren. Wenn du den Befehl `git stash`
ausführst, werden alle nicht-committeten Änderungen im sogenannten Stash gespeichert. Um dir einen Überblick über die
gespeicherten Stashes zu verschaffen, kannst du `git stash list` verwenden. Die zuletzt gespeicherten Änderungen kannst
du mit `git stash pop` wiederherstellen. Dabei werden die Änderungen zurückgebracht und gleichzeitig aus dem Stash entfernt.
Falls du einen bestimmten Stash-Eintrag löschen möchtest, hilft dir der Befehl `git stash drop`.

## Weitere Informationen
Viele Entwicklungsumgebungen bieten eine Unterstützung von Git. Die dafür entwickelten Benutzeroberflächen
können den Umgang mit Git vereinfachen. Außerdem gibt es dedizierte Werkzeuge wie
[GitHub Desktop](https://github.com/apps/desktop), welches sich nicht nur mit Repositories auf GitHub nutzen lässt.

Wenn du dein Wissen über Git vertiefen möchtest, lohnt sich ein Blick in das Buch Pro Git von Scott Chacon und Ben Straub.
Es ist kostenlos online verfügbar, auch in deutscher Übersetzung, unter: https://git-scm.com/book/en/v2.
