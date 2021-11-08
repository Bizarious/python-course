# Lösungen für "Booleans und Funktionen"
# Aufgabe 1

#### Es geht um den letzten Prüfungsversuch eines Studenten. ####
#### Definiere 3 Variablen, die jeweils nur True oder False sein können: ####
#### gelernt, glueck und aufgepasst. ####

gelernt = True
glueck = True
aufgepasst = True

#### Wenn (a) mindestens eine, oder (b) mindestens zwei der drei ####
#### Variablen True sind, hat der Student bestanden und es wird ####
#### True ausgegeben. Implementiere diese beiden Aussagen mithilfe ####
#### der dir bekannten logischen Operationen. ####

# (a) Hier reicht es, alles mit "oder" zu verbinden, weil nur mindestens eines wahr sein muss
bestanden_a = gelernt or glueck or aufgepasst
print(bestanden)

# (b) Hier kann man immer zwei mit "und" verknüpfen, da mindestens zwei wahr sein
# müssen. Anschließend muss man alle Paare mit oder verbinden. Die Klammern
# können weggelassen werden, da und stärker bindet als oder. Sie sind nur für das bessere
# Verständnis hier mit drin.
bestanden_b = (gelernt and glueck) or (gelernt and aufgepasst) or (glueck and aufgepasst)
print(bestanden)

#### Definiere eine weitere Variable: beitrag_bezahlt. ####
#### Es soll angezeigt werden, ob der Student exmatrikuliert wird. ####
#### Dies hängt davon ab, ob er die Studiengebühren bezahlt und ####
#### den letzten Prüfungsversuch bestanden hat. ####
#### Implementiere auch diese Aussage. ####

beitrag_bezahlt = False
exmatrikuliert = not beitrag_bezahlt or not bestanden
