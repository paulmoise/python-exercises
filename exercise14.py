import  re
import iteration_utilities
def wordcount(path):
    with open(path, "r") as file:
        lines = file.readlines();
        nbre_lines = len(lines) #recupère le nombre de ligne
        nbre_characters = 0     #recupère le nombre de caractères
        nbre_words = 0          #recupère le nombre de mot

        for line in lines:
            nbre_characters += len(line)
            modified_line = line[:-1]  #je crois que le \n fausse mon resultat. Donc je prends la chaine jusqu'à l'avant dernier caractère
            list_words = re.split("\s", modified_line)
            nbre_words+=len(list_words)
        print(f"Le nombre de caractères (les espaces inclus) est {nbre_characters}")
        print(f"Le nombre de mots  est {nbre_words}")
        print(f"Le nombre de lignes est {nbre_lines}")
        print(f"Le nombre de mot unique est {nbre_characters}")



wordcount("datasets/cout.txt")

