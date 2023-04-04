'''
calling function inside another function
'''


def name_1():
    return 'name_1'

def name_2():
    n = name_1()

    return f'name_2, {n}'

print(name_2())