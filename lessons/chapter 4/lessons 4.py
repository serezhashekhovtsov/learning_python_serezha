#4.1
pizzas = ['peperon', '4_chees', 'carbonara', 'yagodnya']
for pizza in pizzas:
    print(f'i like {pizza}!')
print('I really love pizza!')

#4.2
animals = ['cat', 'dog', 'bull']
for animal in animals:
    print(f'A {animal} would make a great pet')
print('Any of theese animals would make a great pet')

#4.3
print('_____')
for value in range(1,21):
    print(value)

#4.4
for value in range(1,1000):
    print(value)

#4.5
spisok_2 = list(range(1,1000000))
print(sum(spisok_2))

#4.6
spisok_3 = list(range(1,21,2))
print(spisok_3)

#4.7
threes = list(range(3, 31, 3))
for number in threes:
    print(number)

#4.8
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
    print(cube)

#4.9
squares_123 = [value_1**3 for value_1 in range(1,11)]
for valuee in squares_123:
    print(f'{valuee} ---')

#4.10
pizzas_22 = ['peperon', '4_chees', 'carbonara', 'yagodnya', 'pyperka', 'zhopka']
print(f'The irst three items in the list are: {pizzas_22[:3]}')
print(f'The items from the middle of the list are: {pizzas_22[2:4]}')
print(f'The last three items in the list are: {pizzas_22[3:]}')

#4.11
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")


#4.12

#4.13


