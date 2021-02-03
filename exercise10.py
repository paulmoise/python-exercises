def mot_lettre_repetee(list_words):
    alphabet_letters = "abcdefghijklmnopqrstuvwxyz"
    count_occurence_in_word = 0  #cette variable recupère le nombre d'occurence d'une lettre
    max_occurence_inside_word = 0 #cette variable recupère la plus grande occurence dans un mot
    words_with_max_occurrence = dict()
    for word in list_words:
        max_occurence_inside_word = 0 # réinitialiser l'occurrence maximale avant de passer au mot suivant de la llste
        for letter in alphabet_letters:
            count_occurence_in_word = word.count(letter) # on boucle sur les lettres de l'alphabet et on compte l'occurrence en utilisant la fonction count
            max_occurence_inside_word = max(max_occurence_inside_word, count_occurence_in_word) # recuperer le max du nombre d'occurence de la précédente et celui de la lettre suivante.
        words_with_max_occurrence[max_occurence_inside_word]=word
    maxOccurence = max(words_with_max_occurrence.keys())
    return words_with_max_occurrence.get(maxOccurence)


print(mot_lettre_repetee(["On",  "elementairee", "aa", "effectuee", "plusieurs", "tests", "ce", "matin"]))