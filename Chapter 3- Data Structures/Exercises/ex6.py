guests = [ 'umer', 'waleed']
name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

# umer went home so instead call Bilal.
del(guests[1])
guests.insert(1, 'saqib')

name = guests[0].title()
print(name + ", please come to eat.")

name = guests[1].title()
print(name + ", please come to eat.")

