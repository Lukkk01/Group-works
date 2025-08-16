accounts = []

def main():
    print('Welcome to the International Bank!')
    print('To create an account, enter 1')
    print('To deposit money, enter 2')
    print('To transfer money, enter 3')
    print('To withdraw money, enter 4')
    print('To exit, enter 5')
    print('To log in, enter 6')
    choice = input('Enter here: ')

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit_money()
    elif choice == '3':
        transfer_money()
    elif choice == '4':
        withdraw_money()
    elif choice == '5':
        print("Goodbye")
    elif choice == "6":
        login()
    else:
        print('invalid input')

def create_account():
    print('Create your account')
    name = input('Name: ')
    surname = input('Surname: ')
    age = input('Age: ')
    password = input('Password: ')
    first_deposit = input('Enter your first deposit: ')
    if not first_deposit.isdigit():
        print('Enter a valid amount')
        return
    account = {
        'name': name,
        'surname': surname,
        'age': age,
        'password': password,
        'balance': int(first_deposit)
    }
    accounts.append(account)
    print("account created succesfully!")

def find_account(name, password):
    for account in accounts:
        if account['name'] == name and account['password'] == password:
            return account
    return None

def deposit_money():
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    account = find_account(name, password)
    if not account:
        print('account not found or incorrect password')
        return
    amount = input('Enter the amount of money: ')
    if not amount.isdigit():
        print('invalid amount')
        return
    account['balance'] += int(amount)
    print('deposit successful')

def transfer_money():
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    account = find_account(name, password)
    if not account:
        print('account not found or incorrect password')
        return
    amount = input('Enter amount: ')
    if not amount.isdigit():
        print('invalid amount')
        return
    amount = int(amount)
    if account['balance'] < amount:
        print('not enough money')
        return
    account['balance'] -= amount
    print('successful transfer')

def withdraw_money():
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    account = find_account(name, password)
    if not account:
        print('account not found or incorrect password')
        return
    amount = input('Enter amount: ')
    if not amount.isdigit():
        print('invalid amount')
        return
    amount = int(amount)
    if account['balance'] < amount:
        print('not enough money')
        return
    account['balance'] -= amount
    print('successfully withdrawn')

def login():
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    account = find_account(name, password)
    if not account:
        print('account not found or incorrect password')
        return
    print('welcome back')

main()