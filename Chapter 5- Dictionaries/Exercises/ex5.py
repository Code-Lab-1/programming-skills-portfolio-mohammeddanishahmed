pets = ['tiger','dog','cat']
pets = {
    'animal type': 'lion',
    'name': 'bila',
    'owner': 'ahmed',
    'weight': 68,
    'eats': 'flesh',
}
pets.append(pets)

pets = {
    'animal type': 'dog',
    'name': 'tommy',
    'owner': 'Danish',
    'weight': 6,
    'eats': 'dog treats',
}
pets.append(pets)

pets = {
    'animal type': 'cat',
    'name': 'tommy',
    'owner': 'danish',
    'weight': 37,
    'eats': 'dogs',
}
pets.append(pets)


for pets in pets:
    print(f"\nHere's what I know about { pets['tiger','dog','cat'].title() }:")
    for key, value in pets.items():
        print(f"\t{key}: {value}")