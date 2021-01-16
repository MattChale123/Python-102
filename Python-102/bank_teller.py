def log_in_info():
    user_name = input('Hello, what is your name? If this is new account, then enter your name and skip the account number. ')
    user_account = int(input('Thank %s. Now what is your account number? ' % user_name))
    


class bank_account:

    balance = 25

    def balance_inquire(self):
        print('\n Available Balance is: ', balance)


    def deposit(self):
        amount_entered = float(input('Enter amount to be deposited: '))
        balance += amount_entered
        print('\n Amount Deposited: ', amount_entered)
    

    def withdrawl(self):
        amount_entered = float(input('Enter amount to be withdrawn: '))
        if balance >= amount_entered:
            balance -= amount_entered
            print('\n Amount Withdrawn: ', amount_entered)
            print('\n Updated Balance: ', balance_inquire(self))
        else:
            print('Insufficient Balance  ')

