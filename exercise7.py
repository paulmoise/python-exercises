
def without_vowelA(string):
    vowels = "eiouy"
    str_without_vowel = ""
    for letter in string:
        if letter not in vowels:
            str_without_vowel+=letter
    return str_without_vowel
print(without_vowelA("il fait tres beau ce matin"))

"""
Version of this program using regex
"""