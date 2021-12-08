# Lösungen für "Module und Erweiterte Iteration"

#### 1.a. Definiere eine Klasse Timer mit zwei Funktionen: execute und ####
#### action. Die action Funktion soll leer bleiben (pass). In der ####
#### execute Funktion soll die action Funktion ausgeführt werden und die ####
#### Zeit der Ausführung gestoppt und ausgegeben werden (time.time() benutzen). ####

# Der Sinn hinter diesem "Muster" ist, dass man später neue Klassen
# erstellt, diese hiervon erben lässt und dann die action Methode
# implementiert. Anschließend kann man ganz einfach execute aufrufen und bekommt
# immer das Ergebnis, welches man gerade braucht. Genauers dazu folgt
# im 2. Semester im Modul "Softwaretechnologie".

class Timer:

    def execute(self):
        t1 = time.time()
        self.action()
        t2 = time.time()
        return t2 - t1

    def action(self):
        pass

#### 1.b. Erstelle eine neue Klasse und überschreibe die action Funktion ####
#### mit einer Funktion, die das Programm 3 Sekunden lang 'schlafen legt'. ####
#### Lass dir das Ergebnis der execute Funktion deiner neuen Klasse ausgeben. ####

class SleepTimer(Timer):

    def action(self):
        time.sleep(3)

s = SleepTimer()
s.execute()

#### 2. Importiere itertools ####
#### Erstelle eine neue Klasse die von Timer erbt und in der die action  ####
#### Methode alle 3-, bzw. 5-stelligen Kombinationen der Zahlen von
#### 0 bis 19 als Liste von Tupeln ausgibt. ####
#### a. löse die Aufgabe mit verschachtelten for-Schleifen ####
#### b. löse die Aufgabe mit der itertools.product Funktion

# Dies ist die Lösung fpr b. Für a braucht man 2 Schleifen weniger.
class NaiveLoop(Timer):

    def action(self):
        l = range(20)
        results = []
        for a in l:
            for b in l:
                for c in l:
                    for d in l:
                        for e in l:
                            results.append((a, b, c, d, e))


# Dies ist die Lösung fpr b. Für a muss man einfach nur bei repeat 3 angeben.
class EfficientLoop(Timer):

    def action(self):
        results = []
        for t in itertools.product(range(20), repeat=5):
            results.append(t)


if __name__ == "__main__":
    print(NaiveLoop().execute())
    print(EfficientLoop().execute())
