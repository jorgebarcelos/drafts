'''Dict  creation'''

person = {
    'name': 'John',
    'last_name': 'McArthur',
    'age': 40,
    'adresses': [
        {'street': 'One, 178'},
        {'street': 'Two, 179'}
    ]
}


'''Iteration  over dict key values'''

for key, values in person.items():
    print(f'{key}: {values}')




def dynamic_key(key):
    '''Dynamic key for a dict'''
    person = {}
    person[key] = 'Jorge Bacelos'
    return person

print(dynamic_key('name'))