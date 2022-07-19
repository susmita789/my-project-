#                GUESSING THE NUMBER 

import random 
l = []
def trials(x,list):
    i = 1
    while True:
        n = int(input(f'enter the number between {a} and {b} '))
        if n>x:
            print('wrong guess! The number is greater than te required one')
            i = i+1
        elif n<x:
            print('wrong guess!  The number is smaller than te required one')
            i = i+1
        elif n == x:
            print(f'correct guess! you guess correctly in {i} th trial')
            list.append(i)
            break



a = int(input('Enter the first value - '))
b = int(input('Enter the last value in the range - '))
x = int(input('no of player play the game - '))
mo = random.randint(a,b+1)
for i in range(x):
    print(f'Player {i+1}:')
    trials(mo,l)
    print('\n')

print('Results')

if l[0]>l[1]:
    print('player 2 wins!')
elif l[0]<l[1]:
    print('Player 1 wins!')
elif l[0] ==l[1]:
    print('match tei! Both take same guess.......')