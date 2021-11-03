# Lösungen für "Zahlen, Listen und Schleifen"
# Aufgabe 1

# Man fängt in Python bei 0 an zu zählen.
# Das erste Element einer Liste hat also den Index 0, das zweite die 1 und so weiter.

#### 1. Erstelle eine leere Liste und speicher diese in einer Variable. ####
liste = []

#### 2. Fülle diese Liste nacheinander mit den zahlen 13, 7 und 0. ####

# Hier kann einfach 3 mal hintereinander "append" benutzt werden
liste.append(13)
liste.append(7)
liste.append(0)

#### 3. Addiere das erste und zweite Listenelement und überschreibe ####
#### mit dem Ergebnis das Dritte. ####

# Man kann entweder alles einzeln in Variablen packen,
a = liste[0]
b = liste[1]
liste[2] = a + b

# oder direkt auf die Listenelemente zufreifen
liste[2] = liste[0] + liste[1]

#### 4. Entferne das zweite Element und hänge es hinten an die Liste wieder an. ####

# Hier bietet sich "pop" an, da es ein Listenelement nach Index entfernt
# und zurückgibt
e = liste.pop(1)
liste.append(e)

# oder
liste.append(liste.pop(1))

#### Zusatz: Prüfe, ob das erste Element kleiner ist als das zweite. ####
#### Wenn das so ist, füge hinten an die Liste True an, ansonsten False. ####

# Hier wird die Operation "<" benötigt. Diese Operation gibt direkt
# True oder False zurück, man kann es also sehr kurz fassen
liste.append(liste[0] < liste[1])

# am Ende noch ausprinten
print(liste)
