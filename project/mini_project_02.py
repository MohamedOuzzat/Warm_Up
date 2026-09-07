import math
all=[]
villes=[]
def charger_villes(chemin):
    
    with open(f"{chemin}","r") as file:
        reader = file.readlines()

    for i in reader:
        ph=i.split(" ")
        obj={
             "ville":ph[0],
             "x":ph[1],
             "Y":ph[2]
                }
        
        tup=(ph[-3],ph[-2],ph[-1])
        all.append(obj)
        villes.append(tup)
    for i in villes:
         print(f"{i}\n") 

    print(f"nombre total : {len(villes)}")

charger_villes("ville.txt")


def distance(villeA, villeB):
    X1=float(villeA[-2])
    X2=float(villeB[-2])
    Y1=float(villeA[-1])
    Y2=float(villeB[-1])

    distance = math.sqrt(pow(X2-X1,2)+pow(Y2-Y1,2))
    return distance


def itineraire_greedy(villes):
    close_city=[]
    v=villes.copy()
    
    actuelle = v.pop(0)
    close_city.append(actuelle)
    
    while v:
        plus_proche = min(v, key=lambda ville: distance(actuelle, ville))
        close_city.append(plus_proche)
        v.remove(plus_proche)
        actuelle = plus_proche

    for d in close_city:
        print(f"{d}\n")
    print(len(close_city))

    return close_city
    

itineraire_greedy(villes)


# def distance_totale(itineraire):
#     count=0
#     for i in range(len(itineraire)):
#         count+=distance(itineraire[i],itineraire[i+1])

#     print(count)

# distance(itineraire_greedy(villes))