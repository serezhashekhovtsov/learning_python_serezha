people = ['aric', 'artem', 'zevs', 'dog', 'pryanic']
print("\nSorry, we can only invite two people to dinner.")

name = people.pop()
print(f"\nSorry, {name.title()} there's no room at the table.")

name = people.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = people.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = people[0]
print(f'\n{name.title()} please come to dinner!')

name = people[1]
print(f'{name.title()} please come to dinner!')

del people[0]
del people[1]

print(people)