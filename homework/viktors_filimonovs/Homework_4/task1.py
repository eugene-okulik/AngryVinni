my_dict = {
    'tuple': (1, 4, 56, 3, 5, 56),
    'list': [1, None, 'tekst', False, 0.98, 4, 'tekst45'],
    'dict': {
        'first': 'one',
        'second': 'two',
        'third': 3,
        '4': True,
        'five': None
    },
    'set': {1, 3, 5, 'text', True, 3.4, 'tekst5'}
}

print("last tuple element: ", my_dict['tuple'][-1])

my_dict['list'].append('last')
del my_dict['list'][1]

my_dict['dict'][('i am a tuple',)] = 'any value'
my_dict['dict'].pop('second')

my_dict["set"].add('added element')
my_dict['set'].discard(3.4)

print(my_dict)
