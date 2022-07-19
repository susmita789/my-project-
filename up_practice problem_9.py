#            JUMBLED FUNNY NAMES

import random
number = int(input('Enter the number of friends whoes name you want to enter - '))
name = []
surname = []
for i in range(number):
    f  = input('Enter the complete name of your friend in two words with a gap- ')
    l = f.split()
    name.append(l[0])
    surname.append(l[1])
random.shuffle(surname)
lenght = len(name)
j = 0 
while j < lenght:
    print(f'{name[j]} {surname[j]}')
    j = j+1

print('have fun dont worry for the result, girls look at your surname after marraige!')