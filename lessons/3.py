#3.1
name_friends = ['serezha', 'oleg', 'ayaz']
print(name_friends[0])
print(name_friends[1])
print(name_friends[2])

#3.2
message = f'hello, {name_friends[0].title()}!'
print(message)
message1 = f'hello, {name_friends[1].title()}!'
print(message1)

#3.3
favorite_cars = ['ford focus 2', 'renault koleos']
print(f'Я бы хотел купить машину {favorite_cars[0].title()}!')
print(f'Я бы хотел купить машину {favorite_cars[1].title()}!')

# name.append('variable') - добавление переменной в конец списка
# name[0] = 'variable' - изменение 1 элемента в списке
# spisok = [] - пустой список
# spisok.append('honda') - добавление в пустой список элемента
# spisok.insert(0, 'suzuki') - вставка элемента в позицию 0
# del spisok[0] - удаление элемента 0
# popped_motorcycle = motorcycles.pop() - последний элемент в списке
# spisok.remove('honda') - удаление элемента, когда не знаем номер в списке

#3.4
killed_people = ['satana', 'pryanik', 'zevs']
print(f'{killed_people[0].title()}, пригалашаю тебя на ужин!')
print(f'{killed_people[1].title()}, пригалашаю тебя на ужин!')
print(f'{killed_people[2].title()}, пригалашаю тебя на ужин!')

#3.5
print(f'\n{killed_people[2].title()} не сможет подойти на ужин!')
killed_people[2] = 'afina'
print(f'{killed_people[2].title()}, приглашаю тебя на ужин!')

#3.6
killed_people.insert(0, 'bog')
killed_people.insert(1, 'dog')
killed_people.append('huiymbula')
print(f'\n{killed_people[0].title()}, пригалашаю тебя на ужин!')
print(f'{killed_people[1].title()}, пригалашаю тебя на ужин!')
print(f'{killed_people[2].title()}, пригалашаю тебя на ужин!')
print(f'{killed_people[3].title()}, пригалашаю тебя на ужин!')
print(f'{killed_people[4].title()}, пригалашаю тебя на ужин!')
print(f'{killed_people[5].title()}, пригалашаю тебя на ужин!')

print(f'\nК нам подойдут - {killed_people[0].title()}, {killed_people[1].title()}, {killed_people[-1].title()} на ужин!')

#3.7
print(f'Извините, на ужин пригалаются только {killed_people[0].title()}, {killed_people[1].title()}, а {killed_people[2].title()}, {killed_people[3].title()}, {killed_people[4].title()} не приглашены!')