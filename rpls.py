import random
rock = 3
sizzors = 2
paper = 1
choise = input('>>>')
a = random.randint(1, 3)
if a == 3:
    a = rock
    atext = 'rock'
elif a == 1:
    a = paper
    atext = 'paper'
elif a == 2:
    a = sizzors
    atext = 'sizzors'
print(atext)
if choise == 'rock':
    choise = rock
elif choise == 'paper':
    choise = paper
elif choise == 'sizzors':
    choise = sizzors
if a == 3 & choise == '1':
    print('you win')
elif a == 1 & choise == 3:
    print('computer wins')
elif a > choise:
    print('computer wins')
elif choise == a:
    print('tie')
else:
    print('you win')
