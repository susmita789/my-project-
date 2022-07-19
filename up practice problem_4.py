#                     THE NEXT PALINDROME
def reverse(num):
    s = str(num)
    b =[]
    ls = len(s)
    for i in range(ls):
        b.append(s[i])
    b.reverse()
    z = ''.join(b)
    return z


def palindrom():
    
    eno = int(input('Enter the number whoes next palindrom you want to see '))
    ieno = eno +1 
    while True:
        if str(ieno) == reverse(ieno):
            print(f'{ieno} is a palindrom')
            break
        else:
            ieno = ieno+1    

n = int(input('how many numbers you take to check the next palindrom? '))
for i in range(n):
    palindrom()
  
            

