# YOUR AGE AT 2090
from datetime import date
def age_at_anyyear(year_of_birth,current_year,your_age):
    n = int(input('Enter the year when you wanted to know your age: '))
    try:
        if 1900<n<2100 and n>=year_of_birth:
            if n<=current_year:
                m = n-year_of_birth
                print(f'your age at{n} is {m}')
            elif n>=current_year:
                gap_year = n - current_year
                age = your_age + gap_year
                print(f'your age at {n} is {age}')

        else:
            print('Are you jocking bluddy fool')
    except Exception as e:
        raise Exception('there is something went wrong')

def your_age():
    you = int(input('Enter your birth age or current year: '))
    curyr = date.today().year
    year_d = 2090-curyr
    if len(str(you)) == 2:
        yob = curyr-you
        rest_age = 100-you
        ya_100 = curyr + rest_age
        print(f'you will be 100 in the year of {ya_100}')
        
        aa2090 = you + year_d
        print(f'your age at 2090 is {aa2090}')
        if aa2090>112:
            print('congrats your are the oldest person in planet')

        print('do you want to know your age at any year if yes give 1 and if no then enter 0')
        bb= int(input('Enter 0/1 : '))
        if bb == 0:
            pass
        elif bb ==1:
            age_at_anyyear(yob,curyr,you)
        else:
            print('sorry we dont unstanstand your reply')
    
    
    elif len(str(you)) == 4:
        if you>curyr:
            print('are you jocking with me')
            raise Exception('you deserve nothing')
        elif you<=curyr:
            you_age = curyr - you 
            print(f'At {curyr} your age is {you_age}') 
            rest_100 = 100 - you_age
            year_100 = curyr + rest_100
            print(f'the year when your age is 100 is {year_100}')
            age_2090 = you_age+year_d
            print(f'your age at 2090 is {age_2090}')
            print('do you want to know your age at any year if yes give 1 and if no then enter 0')
            bb= int(input('Enter 0/1 : '))
            if bb == 0:
                pass
            elif bb ==1:
                age_at_anyyear(you,curyr,you_age)
            else:
                print('sorry we dont understand your reply')

your_age()
print('thanks for using')
        


