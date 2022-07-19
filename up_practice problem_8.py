#                     CATCHING OF WRONG MULTIPLICATION TABLE

import random
def ver_tab(n):
    x = random.randint(2,11)
    fake = []
    for i in range(1,11):
        if i ==x:
            fake.append(random.randint(((i-1)*n)+1,((i+1)*n)-1))
        else:
            fake.append(i*n)
    return fake

def susmita(n):
    original = []
    for i in range(1,11):
        original.append(i*n)
    return original


yreq = int(input('Enter the number whoes multiplication table you want - '))
lr = ver_tab(yreq)
print(lr)
ls = susmita(yreq)
print(ls)
 
i = 0
while i<10:
    if lr[i] == ls[i]:
        if i ==9:
            print('Rohan das give you correct multiplication table')
            break
        else:
            i = i+1
    elif lr[i] != ls[i]:
        print(f'{i+1}*{yreq} not equal to {lr[i]}, it is equal to {ls[i]}.')
        print('rohan das is fraud')
        break