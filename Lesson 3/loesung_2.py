# Lösungen für "Booleans und Funktionen"
# Aufgabe 2



#### 1. Definiere eine Funktion, die 3 Variablen (alles bool) ####
#### als Argumente nimmt und True zurückgibt, wenn 2 von 3 ####
#### ebenfalls True sind. Probiere die Funktion aus. ####

# Ist wie in Aufgabe 1
def two_of_three(b1, b2, b3):
    return b1 and b2 or b1 and b3 or b2 and b3

#### Definiere eine Funktion, die die Funktion aus 1. mit allen ####
#### möglichen Kombinationen der Argumente wiederholt aufruft, ####
#### also True True True, True True False, True False True und so weiter. #### 

# Diese dreifach verschachtelte for-Schleife ist nicht unbedingt direkt
# ersichtlich. Spiele im Kopf durch, was hier genau passiert:
# In jeder Iteration wird die Funktion von oben mit anderen Parametern
# aufgerufen und zwar jeweils immer mit den aktuellen Schleifenvariablen
# b1, b2 und b3. Das führt dazu, dass jede mögliche Kombination einmal
# dran kommt.
def alle_varianten():
    for b1 in [True, False]:
        for b2 in [True, False]:
            for b3 in [True, False]:
                result = two_of_three(b1, b2, b3)
                print(f"input: {[b1, b2, b3]} result: {result}")
alle_varianten()
