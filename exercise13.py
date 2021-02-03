
def voyage():
    villes = dict()
    print("Python airlines")
    while True:
        ville = input("Ville: ")
        if(ville != ""):
            nbreHeure = input("Nbre d'heure(s): ")
            villes[ville]=nbreHeure
        else:
            break
    print("Liste des escales:")
    for city, hour in villes.items():
        print(f"{city} {hour},")

voyage()

