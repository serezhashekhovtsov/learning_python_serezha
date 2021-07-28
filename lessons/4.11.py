#4.11
favorite_pizzas = ['four_cheese', 'cheese', 'margarita', 'bacon']
friends_pizzas = favorite_pizzas[:]

favorite_pizzas.append('paperony')
friends_pizzas.append('gorkya')

print('My favorite pizzas are:')
for favorite_pizza in favorite_pizzas:
    print(f'- {favorite_pizza.upper()}')

print('\nMy friends favorite pizzas are:')
for friends_pizza in friends_pizzas:
    print(f'- {friends_pizza.upper()}')
