# Lösungen für "Tupel und Dictionary"
# Aufgabe 1

#### 1. Schreibe eine Funktion, die zwei 2-dimensionale Punkte A und B ####
#### (jeweils als Tupel) entgegennimmt und den Vektor AB ####
#### als Tupel zurückgibt. ####

def vector_zwischen(p1, p2):
    # p1 und p2 sind Tupel (z.B. (5, -2)). Dadurch kann man die Werte in ihnen direkt
    # an Variablen binden, hier also z.B. x1 und y1.
    x1, y1 = p1
    x2, y2 = p2
    return (x2 - x1, y2 - y1)

A = (3, 5)
B = (-1, -2)
print(f"Vector zwischen {A} und {B}: {vector_zwischen(A, B)}")

#### 2. Modifiziere die Funktion so, dass sie nun Vektoren ####
#### beliebiger Dimension berechnen kann. Der Einfachheit halber ####
#### gehen wir davon aus, dass beide Punkte die selbe Dimension haben. ####

def vector_zwischen(p1, p2):
    # wir benutzen eine Liste, da Tupel nicht mehr veränderbar sind,
    # sobald sie einmal erstellt wurden.
    listen_vektor = []
    for i in range(len(p1)):
        listen_vektor.append(p2[i] - p1[i])
    # hier wird die Liste zu einem Tupel gemacht, weil wir ein Tupel
    # zurüclgeben wollen.
    return tuple(listen_vektor)

A = (1,0,4,7,2,4,5)
B = (1,2,3,9,2,5,6)
print(f"Vector zwischen {A} und {B}: {vector_zwischen(A, B)}")
