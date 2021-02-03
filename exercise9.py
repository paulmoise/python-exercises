def somme_pair_impair(list_number):
    sum_index_pair = 0
    sum_index_impair = 0
    for i, value in enumerate(list_number):
        if i%2 == 0:
            sum_index_pair+=value
        else:
            sum_index_impair+=value
    return [sum_index_pair,sum_index_impair]
print(somme_pair_impair([10,20,30,40,50,60]))