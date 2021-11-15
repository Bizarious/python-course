# Lösungen für "Tupel und Dictionary"
# Aufgabe 3

#### 1. Gegeben ist ein Dictionary. Schreibe eine Funktion, welche zählt, ####
#### wie oft jeder Value vorkommt und ein Dictionary ausgibt, indem der ####
#### jeweilige Value auf die Anzahl seines Vorkommens gemappt wird. ####

def count_values(d):
    count = {}
    for i in d:
        # wir iterieren durch die Keys im Dictionary und greifen mit "d[i]" auf
        # das Value zu.
        if d[i] not in count.keys():
            # wenn der Key vorher nicht existierte, können wir einfach 1
            # reinschreiben, weil es ja das erste Vorkommen ist.
            count[d[i]] = 1
        else:
            count[d[i]] += 1
    return count

print("# 3.1:")
print(count_values({1: True, "lksajd": False, None: "ad", 5: 42, "sad": "lsakdjl", 92: 42}))

#### 2. Benutze die in 1. definierte Funktion, um von einem gegebenen ####
#### Dictionary den Value zu bestimmen, der am häufigsten vorkommt. ####

def get_max(d):
    # am Anfang ist max_key None und max_value 0.
    max_key, max_value = None, 0
    for key in d:
        if d[key] >= max_value:
            max_key, max_value = key, d[key]
    return max_key

print("# 3.2:")
print(get_max({"x": 1, "y": 4, "z": 2}))

#### Z. Schreibe eine Funktion, die eine Liste von 2-dimensionalen ####
#### Integer Tupeln entgegen nimmt. Die Tupelelemente sollen addiert werden ####
#### und in einer Ergebnisliste ausgegeben werden. Da es vorkommen kann, ####
#### dass das gleiche Tupel in der Liste zweimal vorkommt, ####
#### soll ein Dictionary benutzt werden, um berechnete Werte zu speichern, ####
#### sodass diese nicht erneut berechnet werden müssen.

def calculate_sums(input_list):
    cache = {}
    output = []
    # da es eine Liste aus 2-dimensionalen Tupeln ist, kann man direkt mit 2
    # Variablen iterieren.
    for a,b in input_list:
        if (a,b) in cache.keys():
            print(f"answer from cache for {(a,b)}")
            output.append(cache[(a,b)])
        else:
            result = a + b
            output.append(result)
            cache[(a,b)] = result
    print(f"finaler cache Zustand: {cache}")
    return output

input_list = [(1, 2), (65, 7), (4, 5), (65, 7)]
print("# 3.Z:")
print(f"result sums: {calculate_sums(input_list)}")
