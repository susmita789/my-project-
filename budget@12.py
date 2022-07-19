from datetime import date
import time
 

#incapsulation
class budget:

    def __init__(self,name,tol_income,food,clothing,study,entertainment,tax):
        self.name = name
        self.tol_income = tol_income
        self.food = food
        self.clothing = clothing
        self.study = study
        self.enjoy = entertainment
        self.tax = tax
        self.remain = tol_income - food - clothing - entertainment - tax - study

    def __str__(self):
        return f'All Information About Your Budget:-\n\tName : {self.name}  \n\tTotal Income : {self.tol_income} \n\tFood :{self.food}\
            \n\tClothing : {self.clothing} \n\tStudy : {self.study}  \n\tEntertainment : {self.enjoy}\
            \n\tTax : {self.tax}  \n\tSaving : {self.remain}'

    def account_detail(self,categori):
        '''categori  simply defines a string'''
        if categori == 'tol_income':
            return self.tol_income
        elif categori =='name':
            return self.name
        elif categori == 'food':
            return self.food
        elif categori == 'cloth':
            return self.clothing
        elif categori == 'study':
            return self.study
        elif categori == 'enjoy':
            return self.enjoy
        elif categori == 'tax':
            return self.tax
        elif categori == 'remain':
            return self.remain

    def tol_expenses(self):
        return self.tol_income - self.remain


class fund_deposit:
    
    def __init__(self,name,categori_str,categori,amount):
        ''' categori_str -- simply represent a sting which named under which categori yu are working
            categori --- it simply represent how much money you have to your account current now
            use account details method in budget class
            amount  -- how much money you want to deposit externally to your selected category
        '''
        self.name = name
        self.categori_str = categori_str
        self.categori = categori 
        self.amount = amount


    def deposit(self):
        self.categori = self.categori+self.amount 
        print(f'your {self.categori_str} account has {self.categori} ruppes after deposition.')
        with open(f'{self.name}_budget_file.txt','a+') as f:
            f.write(f'{date.today()}: {self.amount } is deposited to {self.categori_str} account\n')
            f.write(f'{date.today()}: your net amount in {self.categori_str} categori is {self.categori}\n')
        return self.categori,self.amount


class fund_withdrawl:
    
    def __init__(self,name,categori_str,categori,amount):
        ''' categori_str -- simply represent a sting which named under which categori yu are working
            categori --- it simply represent how much money you have to your account current now,use account de
                 -tails method in budget class
            amount  -- how much money you want to deposit externally to your selected category
        '''
        self.name = name
        self.categori_str = categori_str
        self.categori = categori 
        self.amount = amount


    def withdrawn(self):
        if self.amount> self.categori:
            print(f'{self.amount } is not present in a {self.categori_str} budget')
            return self.categori
        else:    
            self.categori = self.categori-self.amount 
            print(f'your {self.categori_str} account has {self.categori} ruppes after withdrawal')
            with open(f'{self.name}_budget_file.txt','a+') as f:
                f.write(f'{date.today()}: {self.amount } is withdrawn from {self.categori_str} account\n')
                f.write(f'{date.today()}: your net amount in {self.categori_str} categori is {self.categori}\n')
                return self.categori,self.amount

class fund_transfer:

    def __init__(self,name,from_account,f_account_str,to_account,t_account_str,amount):
        '''Name : name of the account holder
           from_account : from which account you wanted to sent money
           f_account_str : denotes the  type of account for doc string
           t_account :give the name where you want to sent money
           t_account_str : denote the type of account where you want to sent money
           amount : give the amount of money you wanted to transfer

        '''
        self.name = name
        self.from_account = from_account
        self.fcat_account = f_account_str
        self.to_account = to_account
        self.tcat_account = t_account_str
        self.amount = amount

    def transfer(self):
        time.sleep(2.0)
        if self.amount > self.from_account:
            print(f'{self.amount} is not available in {self.fcat_account} acount\
                the current balance is {self.from_account}')
            with open(f'{self.name}_budget_file.txt' ,'a+') as f:
                f.write(f'{date.today()}: {self.amount}  is not transferable from {self.fcat_account}\n\
                    \t to {self.tcat_account} due to lack of balance\n')
                   
        elif self.amount == self.from_account:
            print('you cannot transfer any fund by completely make it empty')
        else:
            self.from_account = self.from_account -self.amount
            print(f'{self.amount} is withdrawn from {self.fcat_account} account\n\
                \t remained amount at that account {self.from_account}')
            self.to_account = self.to_account - self.amount
            print(f'{self.amount} is transfered  to {self.tcat_account} account\n\
                \t amount details at that account {self.to_account}')

            with open(f'{self.name}_budget_file.txt' ,'a+') as f:
                f.write(f'{date.today()} : {self.amount} is deducted from {self.fcat_account}and\n\
                    \t the amount at that account is {self.from_account} \n')
                f.write(f'\t {self.amount} is transfered to {self.tcat_account} and \n\
                    \t the current amount at that account is {self.to_account}\n')

        print('we will be glad to give you service')


class percentile_exp:

    def __init__(self,name,total_income,total_expendature):
        self.name = name
        self.total_income = total_income
        self.expense = total_expendature

    def calculation(self):
        percentile_expence =  (self.expense*100)/self.total_income
        print(f'you are spending {percentile_expence}% of your total income as an expendature')









    
        
#Drivers code ----->>

sumi = budget('Susmita',100000,5000,2500,20000,10000,14000)
print(sumi)
f = sumi.account_detail('enjoy')
n = sumi.account_detail('name')
dep = fund_deposit(n,'enjoy',f,2000)
aso = dep.deposit()[0]
wit = fund_withdrawl(n,'enjoy',aso,12000)
print(wit.withdrawn())

        