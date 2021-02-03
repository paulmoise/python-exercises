
def debut_fin(*args):
    param = args[0]
    first_element = param[0]
    last_element = param[-1]
    if type(param) == str:
        return first_element+last_element
    elif type(param) == list:
        return [first_element,last_element]
    elif type(param) == tuple:
        return first_element, last_element

print(debut_fin("python"))