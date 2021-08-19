#3.1
names = ['artem', 'ayaz', 'nikita', 'zhenya', 'ksusha', 'egor', 'nastya']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#3.2
print(f'Hello, {names[0].title()}!')
print(f'Hello, {names[2].title()}!')
print(f'Hello, {names[2].title()}!')

#3.3
vehicles = ['focus_2', 'captur', 'priora', 'clio RS']
print(f'Я бы хотел купить машину {vehicles[0]}')
print(f'Я бы хотел купить машину {vehicles[1]}')
print(f'Я бы хотел купить машину {vehicles[2]}')
print(f'Я бы хотел купить машину {vehicles[3]}')

#3.4
guests = ['guido van rossum', 'jack turner', 'lynn hill']
for guest in guests:
    print(f'Приглашаю {guest} на обед!')

#3.5
guests_1 = ['guido van rossum', 'jack turner', 'lynn hill']
del guests_1[2]
guests_1.insert(0,'ayaz')
print(guests_1)

#3.6
guests_1.insert(0, 'artem')
guests_1.insert(2, 'roma')
guests_1.append('serezha')
print(guests_1)

#3.7
name_1 = guests_1.pop()
print(guests_1)
name_2 = guests_1.pop()
print(guests_1)
name_3 = guests_1.pop()
print(guests_1)
print(name_1, name_2, name_3)

print(len(guests_1))

#3.8
print(f'___________')
favorite_country = ['russia', 'georgia', 'turkey', 'usa', 'canada', 'abkhazia', 'new Zealand', 'finland']
print(favorite_country)
print(sorted(favorite_country))

print(sorted(favorite_country, reverse=True))

#3.9

#3.10
spisok = []



