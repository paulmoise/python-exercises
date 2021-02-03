#Devinette

"""Ecris une fonction nommée `devinette` qui ne prend aucun argument. Quand on l'exécute, elle
choisit un nombre aléatoire en 0 et 100 (inclus)et demande à l'utilisateur de deviner ce nombre.
A chaque fois que l'utilisateur entre un nombre, le programme affiche l'une de ces phrases :

* Trop grand
* Trop petit
* Exact

Si l'utilisateur a choisit correctement, le programme s'arrete. Sinon,
le programme demande encore à l'utilisateur de rentrer un nouveau nombre jusqu'à ce qu'il
trouve la bonne solution et s'arrête.

> Aide : Cherche le module `random` de Python pour générer un nombre aléatoirement.

Dans cette version du programme on donne 3 essais a lutilisateur

"""

from random import randint, seed

seed()
def devinette():
    """

    :return:
    """
    nombre_essai = 3
    randomValue = randint(0,100)
    userValue = int(input("Quel nombre ai-je choisi?\n"))
    while randomValue != userValue and nombre_essai > 1:
        nombre_essai -= 1
        if userValue > randomValue:
            print("Trop grand")
            print(f"Il vous reste {nombre_essai} essai(s)")
            userValue = int(input("Quel nombre ai-je choisi? \n"))
        elif userValue < randomValue:
            print("Trop petit")
            print(f"Il vous reste {nombre_essai} essai(s)")
            userValue = int(input("Quel nombre ai-je choisi? \n"))



        #print(nombre_essai)

    if(nombre_essai > 0 and randomValue == userValue):
        print("Exact")
    else:
        print("Vous avez epuise le nombre d'essai")

devinette()