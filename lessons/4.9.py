kub = [value**3 for value in range(1,11)]
print(kub)


players = ['charles', 'martina', 'michael', 'florence', 'eli', 'ayaz']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

players_1 = players[:]


players.append('nikita')
players_1.append('zhopa')

print(players_1)
print(players)