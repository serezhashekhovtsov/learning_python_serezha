cars = ['audi', 'bmw', 'subaru', 'toyota']

#for car in cars:
    #if car == 'bmw':
        #print(car.upper())
    #else:
        #print(car.title())

#5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print(car == 'subaru1')

print(2 > 4)
print(3 == 4)
print(3 < 5)
print(2==2)
print(22 >= 22)

#5.2
stroka_1 = 'FFdfsdsfd'
stroka_2 = 'DDasddasad'
print(f'\n -- {stroka_1 == stroka_2}')
print(f'--- {stroka_1.lower() == stroka_1}')
print(3 > 4)
print(3 < 4)
age = 18
age_1 = 45
print(f'\n --{age >= 18 and age <= 45}')
print(f'\n --{age < 17 and age <= 45}')
print(f'\n ❆❆❆ {age < 17 or age <= 45}')

spisok = 'vaz' in cars
spisok_3 = 'audi' not  in cars
spisok_2 = 'audi' in cars

print(f'\n ❆❆❆-- {spisok}, {spisok_2}, {spisok_3}')

