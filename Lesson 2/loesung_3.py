# Lösungen für "Zahlen, Listen und Schleifen"
# Aufgabe 3

#### 1. Definiere ein Passwort. Erfrage vom Nutzer solange dieses Passwort, ####
#### bis er es richtig eingegeben hat. ####

passwd = "meinpasswort" # ein Passwort als String abspeichern
# Hier bietet sich eine Endlosschleife an, da wir den Nutzer potentiell
# unendlich lange nach dem Passwort fragen müssen
while True:
    i = input("Passwort eingeben: ")
    # Input wird vom Nutzer verlangt und als "i" gespeichert
    if i == passwd:
        # wenn der Input gleich dem Passwort ist, können wir aus der Schleife raus
        print("Passwort korrekt")
        break # bricht die Schleife ab
    else:
        # Wenn der Input nicht gleich dem Passwort ist, machen wir einfach
        # garnichts, da die Schleife von selbst weitermacht
        print("Passwort inkorrekt")

#### 2. Sammle alle falsch eingegebenen Passwörter in einer Liste und ####
#### gebe diese Liste am Ende als ganzes aus. Gib zusätzlich noch ####
#### die Anzahl der benötigten Versuche aus. ####

falsch = [] # Liste für falsche Passwörter
passwd = "meinpasswort"
while True:
    i = input("Passwort eingeben: ")
    if i == passwd:
        print("Passwort korrekt")
        break
    else:
        # wir fügen den Input an die Liste an, wenn er falsch war
        falsch.append(i)
        print("Passwort inkorrekt")

print(f"Falsche Passwörter: {falsch}")
# die len()-Funktion gibt die Länge einer Liste aus
print(f"Anzahl falsche Passwörter: {len(falsch)}")

#### 3. Erlaube nur eine maximale Anzahl von Versuchen. ####
#### Lass den Nutzer über das Terminal diese Anzahl vorher eingeben. ####

# Wir müssen den input mit "int()" in eine Zahl konvertieren,
# da er sonst ein String wäre #
grenze = int(input("Maximale Anzahl Versuche: "))
# Die Variable "aktuelle_anzahl" wird hier auf 0 gesetzt
aktuelle_anzahl = 0
falsch = []
passwd = "meinpasswort"
# Wir modifizieren die Schleifenbedingung. Jetzt ist sie nicht mehr immer True,
# sondern hängt davon ab, ob aktuelle_anzahl noch kleiner ist als grenze
while aktuelle_anzahl < grenze:
    # aktuelle_anzahl wird immer um 1 erhöht, sobald wir in die Schleife gehen
    aktuelle_anzahl += 1
    i = input("Passwort eingeben: ")
    if i == passwd:
        print("Passwort korrekt")
        break
    else:
        falsch.append(i)
        print("Passwort inkorrekt")

print(f"Falsche Passwörter: {falsch}")
print(f"Anzahl falsche Passwörter: {len(falsch)}")
