#              PALIDROMIFY THE LIST

def reverse(num):
    s = str(num)
    b =[]
    ls = len(s)
    for i in range(ls):
        b.append(s[i])
    b.reverse()
    z = ''.join(b)
    return z


def palindrom(eno,index,list):
    
    
    ieno = eno +1 
    while True:
        if str(ieno) == reverse(ieno):
            list[index] = ieno
            break
        else:
            ieno = ieno+1    


user = int(input('Enter the number of elements you want to enlist in your list - '))
l = []
for i in range(user):
    num = int(input(f'Enter the {i+1}th element - '))
    l.append(num)


for i in range(len(l)):
    if l[i] >10:
        palindrom(l[i],i,l)
    else:
        pass

print(l)