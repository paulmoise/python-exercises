
# def without_vowel(string):
#     vowels = "aeiouy"
#     str_without_vowel = ""
#     for letter in string:
#         if letter not in vowels:
#             str_without_vowel+=letter
#     return str_without_vowel
# print(without_vowel("python"))


def without_vowel(string):
    vowels = "aeioyu"
    for c in vowels:
        for letter in string:
            if c == letter:
                print(c)
                str = string.replace(letter,"")
                string = str
    return string
print(without_vowel("python"))
"""
Version of this code using regex
"""
# import  re
#
# def without_vowelV2(string):
#     vowels = "aeiouy"
#     regex = re.compile('[aeiouy]')
#     print(regex.sub("",string))
#     #return string
#
# without_vowelV2("python")
