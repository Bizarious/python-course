# Lösungen für "Zahlen, Listen und Schleifen"
# Aufgabe 2

#### 1. Erstelle eine leere Liste und fülle diese ####
#### mithilfe einer for-Schleife mit den Zahlen 1 bis 100. ####

# Das i ist die Variable, die sich in jeder Iteration verändert.
# Die range()-Funktion gibt hier die Zahlen 1 bis 100 zurück. Zu beachten ist,
# dass als rechtes Argument 101 stehen muss, weil sie immer eins weniger ausgibt.
liste = []
for i in range(1, 101):
    liste.append(i)
print(f"1 bis 100: {liste}")

#### 2. Addiere alle Zahlen in der Liste zusammen und gib das Ergebnis aus. ####

# Das geht mit einer for-Schleife, bei der das i durch die Liste geht
# und nach jeder Iteration den nächsten Wert in der Liste annimmt. Es ist dann
# also eine Zahl
ergebnis = 0
for i in liste:
    ergebnis += i # Abkürzung für "ergebnis = ergebnis + i"

# Man kann alternativ auch die sum()-Funktion benutzen, die wir so aber
# nicht beahndelt haben
ergebnis = sum(liste)
print(f"Ergebnis: {ergebnis}")

#### 3. Erstelle zwei neue leere Listen, eine für gerade und eine für ####
#### ungerade Zahlen. Iteriere nun durch die originiale Liste und ordne ####
#### die Elemente den gerade erstellten Listen zu. ####

gerade = [] # Liste für gerade Zahlen
ungerade = [] # Liste für ungerade Zahlen
for i in liste:
    # am intuitivsten geht es mit einer if-Abfrage
    if i % 2 == 0:
        # wenn die Zahl modulo 2 null ist (also glatt durch 2 teilbar ist),
        # wird sie an gerade angehangen
        gerade.append(i)
    else:
        # wenn die Zahl modulo 2 nicht null ist (also nur mit Rest
        # durch 2 teilbar ist), wird sie an ungerade angehangen
        ungerade.append(i)

print(f"Gerade Zahlen: {gerade}")
print(f"Ungerade Zahlen: {ungerade}")
