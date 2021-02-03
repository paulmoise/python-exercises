
menu = { "Chawarma":1000, "Burger":2500, "Cafe": 750, "Ataxi": 300, "Heineken": 500,
         "Pain": 200, "Spaghetti": 500, "Gari": 300}

def restaurant():
    commande_price = 0
    menu_keys = menu.keys()
    while True:
        commande = input("Commande ")
        if commande != "" and commande not in menu_keys:
            print(f"Nous n'offrons pas de {commande} aujourdhui. ")
        elif commande in menu_keys:
            price = menu.get(commande)
            commande_price+=price
            print(f"{commande} coute {price} FCFA, total est {commande_price} FCFA")
        else:
            break
    print(f"Votre total est {commande_price} FCFA \n")

restaurant()