class Bank:

    num_customers = 0;

    def __init__(self):
        self.customers = []

    def add(self, customer):
        self.num_customers += 1
        customer.ID = self.num_customers
        self.customers.append(customer)


class Customer:

    def __init__(self, first, last, age):
        self.ID = 0
        self.first = first
        self.last = last
        self.age = age
        self.accounts = []


class Account:

    def __init__(self):
        self.money = 0

    def deposit(self, amount):
        if amount > 0:
            self.money += amount
        else:
            print("\nError.")

    def withdraw(self, amount, customer):
        if amount > 0 and self.money - amount > 0:
            self.money -= amount
            return amount
        else:
            print("\nInsufficient funds.")


class Savings(Account):

    def __init__(self):
        super().__init__()
        self.type = "Savings"


class Checking(Account):

    def __init__(self):
        super().__init__()
        self.type = "Checking"


class Retirement(Account):

    def __init__(self):
        super().__init__()
        self.type = "Retirement"

    def withdraw(self, amount, customer):
        if int(customer.age) < 67:
            print("\nToo young to withdraw.")
            return
        if amount > 0 and self.money - amount > 0:
            self.money -= amount
            return amount
        else:
            print("\nInsufficient funds.")


def deposit(customer):
    print("Deposit to which account?")
    if customer.accounts:
        for account in enumerate(customer.accounts):
            print(account[0], account[1].type)
        print("\nEnter the number of the desired account.")
        account = int(input(">>"))
        if account < len(customer.accounts):
            print("Current balance:", customer.accounts[account].money)
            amount = int(input("How much will you deposit?\n>>"))
            customer.accounts[account].deposit(amount)
            print("New balance:", customer.accounts[account].money)
            mainMenu(customer)
        else:
            print("\nAccount does not exist.")
            mainMenu(customer)
    else:
        print("\nCustomer has no accounts.\n")
        mainMenu(customer)


def withdraw(customer):
    account = None
    print("\nWithdraw from which account?")
    if customer.accounts:
        for account in enumerate(customer.accounts):
            print(account[0], account[1].type)
        print("\nEnter the number of the desired account.")
        account = int(input(">>"))
        print("\nCurrent balance:", customer.accounts[account].money)
        amount = int(input("How much will you withdraw?\n>>"))
        customer.accounts[account].withdraw(amount, customer)
        print("\nNew balance:", customer.accounts[account].money)
        mainMenu(customer)
    else:
        print("\nCustomer has no accounts.\n")
        mainMenu(customer)


def create(customer):
    print("\nSelect Account Type:\n")
    print("1. Checking")
    print("2. Savings")
    print("3. Retirement")
    choice = input(">>")
    if choice == "1":
        new = Checking()
        customer.accounts.append(new)
        mainMenu(customer)
    elif choice == "2":
        new = Savings()
        customer.accounts.append(new)
        mainMenu(customer)
    elif choice == "3":
        new = Retirement()
        customer.accounts.append(new)
        mainMenu(customer)
    else:
        create(customer)



def mainMenu(customer):
    print("\n", customer.first, customer.last, ", what would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. New Account")
    print("4. Done")
    selection = input(">>")

    if str(selection) == "1":
        deposit(customer)

    elif str(selection) == "2":
        withdraw(customer)

    elif str(selection) == "3":
        create(customer)

    elif str(selection) == "4":
        firstMenu()

    else:
        mainMenu(customer)


def newCustomer():
    print("\nWelcome to Nerd Bank!\n")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    age = input("Enter your age: ")
    new = Customer(first, last, age)
    bank.customers.append(new)
    print("\n\tYour new customer ID is:", new.ID, "\n")
    mainMenu(new)

def oldCustomer():

    customer = None
    ID = input("Enter your customer ID, or press enter: ")
    try:
        ID = int(ID)
    except:
        first = input("Enter your first name: ")
        last = input("Enter your last name: ")
        for person in bank.customers:
            if first == person.first and last == person.last:
                customer = person
                mainMenu(customer)
        print("No match found...")

    print(ID, "LEN",len(bank.customers))
    if ID > len(bank.customers):
        print("\nCustomer does not exist.\n")
        firstMenu()
    elif ID is not None:
        customer = bank.customers[ID]
    else:
        print("\nCustomer does not exist.\n")
        firstMenu()

    if customer:
        mainMenu(customer)
    else:
        print("\nCustomer does not exist.\n")
        firstMenu()


def firstMenu():
    print("1. New Customer")
    print("2. Returning Customer")
    choice = input(">>")
    if choice == "1":
        newCustomer()
    elif choice == "2":
        oldCustomer()
    else:
        firstMenu()


bank = Bank()
#dude = Customer("Jack", "Jackson", 32)
#bank.add(dude)
firstMenu()
