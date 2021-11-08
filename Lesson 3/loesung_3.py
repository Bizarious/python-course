# Lösungen für "Booleans und Funktionen"
# Aufgabe 3

#### 1. Definiere eine Funktion, die eine Liste als Argument entgegennimmt. ####
#### Die Funktion soll True zurückgeben, wenn alle Zahlen in der Liste ####
#### kleiner als 10 sind, ansonsten soll sie False zurückgeben. ####

def liste_kleiner_zehn(zahlen):
    for zahl in zahlen:
        # sobald eine Zahl größer oder gleich 10 ist, wird False zurückgegeben
        # und die Funktion beendet
        if zahl >= 10:
            return False
    # wenn es bis hierhin gekommen ist, dann waren alle Zahlen kleienr 10
    # und es kann True zurückgegeben werden
    return True

# Test
print(f" negativ Test: {liste_kleiner_zehn([2,3,1,3,4,5,10,1])}")
print(f" positiv Test: {liste_kleiner_zehn([2,3,1,3,4,5,6,1])}")

#### 2. Definiere eine Funktion, welche eine Liste aus Integern ####
#### als erstes Argument (die Zahlen) und einen Integer als zweites Argument ####
#### (der Teiler) entgegennimmt. Die Funktion soll eine neue Liste ####
#### zurückgeben, die die originalen Zahlen geteilt durch den Teiler enthält. ####
#### Gib dem zweiten Argument als Default-Wert die 2. ####

def liste_teilen(zahlen, teiler=2):
    geteilte_zahlen = []
    for zahl in zahlen:
        geteilte_zahl = zahl / teiler
        geteilte_zahlen.append(geteilte_zahl)
    return geteilte_zahlen

# mit Teiler angegeben
print(f"liste teilen, kein default {liste_teilen([3,15,11,15,78], 5)}")
# ohne Teiler (wird als 2 behaldelt)
print(f"liste teilen, default {liste_teilen([3,15,11,15,78])}")

#### 3. Definiere eine Funktion, die die beiden Funktionen aus 1. und 2. ####
#### verwendet. Die Funktion soll eine Liste von Zahlen so lange ####
#### durch 2 teilen, bis alle Zahlen der Liste kleiner als 10 sind.

def liste_teilen_bis_kleiner_zehn(zahlen):
    while not liste_kleiner_zehn(zahlen):
        # wichtig ist hier, dass "zahlen" jedes mal überschrieben wird und
        # keine neue Liste angelegt wird. Macht man das nicht, so arbeitet er
        # immer auf der unveränderten Liste und wird niemals fertig.
        zahlen = liste_teilen(zahlen)
        print(f"geteilt: {zahlen}")
    return zahlen
print(f'teilen bis kleiner 10: {liste_teilen_bis_kleiner_zehn([342, 5253, 234, 234, 24])}')
