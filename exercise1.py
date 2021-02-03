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

"""

from random import randint, seed

seed()
# def devinette():
#     randomValue = randint(0,100)
#     userValue = int(input("Quel nombre ai-je choisi?\n"))
#     while randomValue != userValue:
#         if userValue > randomValue:
#             print("Trop grand")
#         elif userValue < randomValue:
#             print("Trop petit")
#         userValue = int(input("Quel nombre ai-je choisi? \n"))
#     print("Exact")
# def devinette():
#     randomValue = randint(0,100)
#     while True:
#         userValue = int(input("Quel nombre ai-je choisi? \n"))
#         if userValue > randomValue:
#             print("Trop grand")
#         elif userValue < randomValue:
#             print("Trop petit")
#         else:
#             print("Exact")
#             break
# devinette()


def devinette():
    randomValue = randint(0,100)
    nombre_essai = 3
    while nombre_essai > 0:
        userValue = int(input("Quel nombre ai-je choisi? \n"))
        if randomValue == userValue:
            print("Exact bien joue !")
            break
        if userValue > randomValue:
            print(f"Trop grand, il vous reste {nombre_essai}")
        elif userValue < randomValue:
            print(f"Trop petit, il vous reste {nombre_essai}")
        nombre_essai-=1
devinette()