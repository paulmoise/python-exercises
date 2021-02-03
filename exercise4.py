lastName = input("Quel est votre nom? \n")
firstName = input("Quel est votre Prenom? \n")
email = f"{lastName.lower()}_{firstName.lower()}@pythonboss.com"
print(email)