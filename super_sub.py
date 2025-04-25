animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }
birds = {'Robin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'birds is a superset of animals: {animals.issuperset(birds)}')

print(f'birds is a superset of animals: {birds.issuperset(animals)}')

print(birds <= animals)
print(animals >= birds)

print('*' * 80)

garden_birds = {'Swallow', 'Wren'}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds)

print('*' * 80)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds >= more_birds)
