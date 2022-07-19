#snake water gun
print('Welcome To Snake Water Gun Game Ceremany')
def yourgame():
    dic ={'snake':'s','water':'w','gun':'g'}
    mylist = list(dic.values())
    import random


    print('snake - s')
    print('water - w')
    print('gun - g')
    locate =[]
   #in locate we measure no of wrong input
    y_point = 0
    y_list = []
    c_point = 0
    c_list = []
    i = 1
    while i < 11:
        x = random.choice(mylist)
        y_turn1 = input('give your input--')
        y_turn = y_turn1.lower()
        if y_turn =='s' and  x =='w':
            
            print('you win')
            y_point += 1
            y_list.append(1)

        elif y_turn == 's' and x =='s':
            print('tie')

        elif y_turn =='s' and x == 'g':
            print('you lose')
            c_point += 1
            c_list.append(1)  

        elif y_turn =='g' and  x =='w':

            print('you lose')
            c_point += 1
            c_list.append(1)

        elif y_turn == 'g' and x =='s':
            print('you win')
            y_point += 1
            y_list.append(1) 

        elif y_turn =='g' and x == 'g': 
            print('tie')

        elif y_turn =='w' and  x =='s':

            print('you lose')
            c_point += 1
            c_list.append(1)

        elif y_turn == 'w' and x =='g':
            print('you win')
            y_point += 1
            y_list.append(1) 

        elif y_turn =='w' and x == 'w': 
            print('tie')

        else:
            locate.append(1)
            print('you have given some wrong input try again')


        i =i+1
    print('10 turns over')
    if y_point>c_point :

        try:    
            print(f'you win with point {y_point}')
            print(f'you win {len(y_list)} times')
            tei=10-len(locate)-y_point-c_point
            print(f'no of teis {tei}')
        except Exception as e:
            print(e)


    elif c_point>y_point :
        try:

            print(f'computer win with point {c_point}')
            print( f'computer  win {len(c_list)} times')
            tei=10-len(locate)-y_point-c_point
            print(f'no of teis {tei}') 
             
        except Exception as e:
            print(e)


    else:
        if c_point == y_point:
            print('match tei' )


    print('thanks for playing ')
    print('wish you all the best for next time')
    playagain()

def playagain():
    
    print('lets play again!!')
    print('let me know your dicision')
    print('type y for yes ,n for no')
    gowith1 = input('y or n --')
    gowith =gowith1.lower()
    if gowith == 'y':
      yourgame()
    elif gowith == 'n':
        print('thanks for joining')
    else:
        print('Something wrong you have been printed sorry but try again')
        playagain()  

#drivers comment
yourgame()
        