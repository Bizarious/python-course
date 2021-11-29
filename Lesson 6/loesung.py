# Lösungen für "Vererbung und Module"

#### 1. Definiere eine Klasse Fahrzeug mit folgenden Eigenschaften: ####
####    Attribute: speed, preis ####
####    Methode: hupen() ####
####    Methode: info() ####

class Fahrzeug:

    def __init__(self, preis, speed):
        self.preis = preis
        self.speed = speed

    def hupen(self):
        print("Huuup")

    def info(self):
        return f"Preis: {self.preis} €, Speed: {self.speed} km/h"

#### 2. Füge eine weitere Methode fahren(dauer) hinzu, die eine Dauer ####
#### entgegen nimmt. Sie soll die Distanz zurückgeben, die in der ####
#### angegebenen Zeit zurückgelegt wurde. ####

class Fahrzeug:

    def __init__(self, preis, speed):
        self.preis = preis
        self.speed = speed

    def hupen(self):
        print("Huuup")

    def info(self):
        return f"Preis: {self.preis} €, Speed: {self.speed} km/h"

    def fahren(self, dauer):
        return dauer * self.speed

#### 3. Definiere die Klasse PKW und LKW. Beide sollen von Fahrzeug erben. ####
#### Der LKW soll außerdem hupen überschreiben (anderes Geräusch ausgeben). ####

class LKW(Fahrzeug):

    def hupen(self):
        print("HUUUUUP!")

class PKW(Fahrzeug):
    pass

#### 4. Erweiterung der Klassen ####
#### PKW: ####
####    alle PKWs sollen 30.000 € kosten und 180 km/h schnell sein ####
####    zusätzliche Attribute: personen_zahl ####
####    info() Methode üebrschreiben: soll personen_zahl mit ausgeben ####
#### LKW: ####
####    alle LKWs sollen 200.000 € kosten und 80 km/h schnell sein ####
####    zusätzliche Attribute: laderaum ####
####    info() Methode üebrschreiben: soll laderaum mit ausgeben ####

class LKW(Fahrzeug):

    def __init__(self, laderaum):
        super().__init__(200000, 80)
        self.laderaum = laderaum

    def hupen(self):
        print("HUUUUUP!")

    def info(self):
        return super().info() + f" Laderaum: {self.laderaum}"

class PKW(Fahrzeug):

    def __init__(self, personen_zahl):
        super().__init__(30000, 180)
        self.personen_zahl = personen_zahl

    def info(self):
        return super().info() + f" Personenzahl: {self.personen_zahl}"

#### Zusatz: Definiere eine Panzer Klasse, die auch von Fahrzeug erbt. ####
#### Panzer sollen 6.000.000 € kosten, 70 km/h schnell fahren und eine ####
#### Anzahl von Munition haben. Außerdem soll ein Panzer schießen können, ####
#### wobei Munition verbraucht wird. Ist keine Munition mehr vorhanden, ####
#### so kann er keinen Schuss mehr abgeben. Beim Schießen soll zudem 'Feuer!' ####
#### ausgegeben werden, wenn der Schuss erfolgt.

class Panzer(Fahrzeug):

    def __init__(self, anzahl_munition):
        super().__init__(6000000, 70)
        self.anzahl_munition = anzahl_munition

    def schiessen(self):
        if self.anzahl_munition > 0:
            print("Feuer!")
            self.anzahl_munition -= 1
        else:
            print("Keine Munition!")

    def info(self):
        return super().info() + f" Munition: {self.anzahl_munition}"
