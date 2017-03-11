class Bank:

    #Class for containing customers, and generating customer IDs.

    num_customers = 0;

    def __init__(self):
        self.customers = []

    def add(self, customer):
        self.num_customers += 1
        customer.ID = self.num_customers
        self.customers.append(customer)


class Customer:

    #Customer class contains identifying information for each
    #customer, such as name. Also contains all of the customer's
    #accounts.

    def __init__(self, first, last, age):
        self.ID = 0
        self.first = first
        self.last = last
        self.age = age
        self.accounts = []

    def information(self):
        print("")
        if self.accounts:
            for account in self.accounts:
                print(account.type, "has a balance of", account.money)
        else:
            print("No accounts found.")


class Account:

    #Account parent class. Contains money, and has basic
    #deposit and withdraw abilities.

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

    #Subtype of account.

    def __init__(self):
        super().__init__()
        self.type = "Savings"


class Checking(Account):

    #Subtype of account.

    def __init__(self):
        super().__init__()
        self.type = "Checking"


class Retirement(Account):

    #Subtype of account. Only able to withdraw from this type
    #after age 67.

    def __init__(self):
        super().__init__()
        self.type = "Retirement"

    def withdraw(self, amount, customer):
        #Redefinition of withraw to prevent the action until
        #age 67
        if int(customer.age) <= 67:
            print("\nToo young to withdraw.")
            return
        if amount > 0 and self.money - amount > 0:
            self.money -= amount
            return amount
        else:
            print("\nInsufficient funds.")


class MMF(Account):

    #Subtype of account. The Money Market Fund is only able to
    #be changed (deposit/withdrawl) twice per month (per run).

    def __init__(self):
        super().__init__()
        self.type = "Money Market Fund"
        self.transactions = 0

    def deposit(self, amount):
        #Redefinition of deposit to limit transactions to 2.
        if self.transactions < 2:
            if amount > 0 and self.transactions < 2:
                self.money += amount
                self.transactions += 1
            else:
                print("\nError.")
        else:
            print("\nMontly transaction limit already met.")

    def withdraw(self, amount, customer):
        #Redefinition of withdraw to limit transactions to 2.
        if self.transactions < 2:
            if amount > 0 and self.money - amount > 0:
                self.money -= amount
                self.transactions += 1
                return amount
            else:
                print("\nInsufficient funds.")
        else:
            print("\nMontly transaction limit already met.")


def deposit(customer, bank):

    #Provides interaction for depositing funds into selected account.

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
            mainMenu(customer, bank)
        else:
            print("\nAccount does not exist.")
            mainMenu(customer, bank)
    else:
        print("\nCustomer has no accounts.\n")
        mainMenu(customer, bank)


def withdraw(customer, bank):

    #Provides interaction for withdrawing money from the given account.

    account = None
    print("\nWithdraw from which account?")
    if customer.accounts:
        for account in enumerate(customer.accounts):
            print(account[0], account[1].type)
        print("\nEnter the number of the desired account.")
        account = int(input(">>"))
        if account > len(customer.accounts):
            print("\nAccount does not exist.")
            mainMenu(customer, bank)
        print("\nCurrent balance:", customer.accounts[account].money)
        amount = int(input("How much will you withdraw?\n>>"))
        customer.accounts[account].withdraw(amount, customer)
        print("\nNew balance:", customer.accounts[account].money)
        mainMenu(customer, bank)
    else:
        print("\nCustomer has no accounts.\n")
        mainMenu(customer, bank)


def create(customer, bank):

    #Provides interaction to the user for building and adding
    #an account of a user chosen type.

    print("\nSelect Account Type:\n")
    print("1. Checking")
    print("2. Savings")
    print("3. Retirement")
    print("4. Money Market Fund")
    choice = input(">>")
    if choice == "1":
        new = Checking()
        customer.accounts.append(new)
        mainMenu(customer, bank)
    elif choice == "2":
        new = Savings()
        customer.accounts.append(new)
        mainMenu(customer, bank)
    elif choice == "3":
        new = Retirement()
        customer.accounts.append(new)
        mainMenu(customer, bank)
    elif choice == "4":
        new = MMF()
        customer.accounts.append(new)
        mainMenu(customer, bank)
    else:
        create(customer)



def mainMenu(customer, bank):

    #Once a customer has been added or found, this menu shows
    #them each of their options.

    print("\n", customer.first, customer.last, ", what would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. New Account")
    print("4. Balance Report")
    print("5. Done")
    selection = input(">>")

    if str(selection) == "1":
        deposit(customer, bank)

    elif str(selection) == "2":
        withdraw(customer, bank)

    elif str(selection) == "3":
        create(customer, bank)

    elif str(selection) == "4":
        customer.information()
        mainMenu(customer, bank)

    elif str(selection) == "5":
        firstMenu(bank)

    else:
        mainMenu(customer, bank)


def newCustomer(bank):

    #Provides interaction for adding a new customer to the bank.

    print("\nWelcome to Nerd Bank!\n")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    age = input("Enter your age: ")
    new = Customer(first, last, age)
    bank.customers.append(new)
    print("\n\tYour new customer ID is:", new.ID, "\n")
    mainMenu(new, bank)

def oldCustomer(bank):

    #Provides interacton for finding an existing customer and their
    #accounts (if any).

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
                mainMenu(customer, bank)
        print("\nNo match found...\n")
        firstMenu(bank)

    if ID > len(bank.customers):
        print("\nCustomer does not exist.\n")
        firstMenu(bank)
    elif ID is not None and bank.customers:
        customer = bank.customers[ID]
    else:
        print("\nCustomer does not exist.\n")
        firstMenu(bank)

    if customer:
        mainMenu(customer, bank)
    else:
        print("\nCustomer does not exist.\n")
        firstMenu(bank)


def firstMenu(bank):

    #Starting point for user interacton.

    print("1. New Customer")
    print("2. Returning Customer")
    print("3. Close Program")
    choice = input(">>")
    if choice == "1":
        newCustomer(bank)
    elif choice == "2":
        oldCustomer(bank)
    elif choice == "3":
        return
    else:
        firstMenu(bank)


