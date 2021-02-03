
def ordonne_str(string):
    letters =[]
    for c in string:
        letters.append(c)
    letters.sort()
    return ''.join(letters)

print(ordonne_str("bca"))