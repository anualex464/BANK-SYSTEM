class Bank_Account:
    def __init__(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        # Assuming we have a list of valid usernames and passwords
        valid_users = ["user1", "user2", "user3"]
        valid_passwords = ["pass1", "pass2", "pass3"]

        if username in valid_users and password == valid_passwords[valid_users.index(username)]:

            print("Login successful!")
        else:
            print("Invalid username or password.")
            exit("try again")

        self.balance = 0
        print("Welcome !")

    def choice(self):
        while True:
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Balance enquiry')
            print('4. Logout')

            choice = int(input('Enter your choice: '))

            if choice == 1:
                amount = float(input("Enter amount to be deposited: "))
                self.balance += amount
                print("Amount Deposited: ", amount)
                print("Balance: ", self.balance)

            elif choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                if self.balance >= amount:
                    self.balance -= amount
                    print("You withdraw: ", amount)
                    print("Balance: ", self.balance)
                else:
                    print("Insufficient balance ")
            elif choice == 3:
                print("Available Balance=", self.balance)
            elif choice == 4:
                print('logout successfully')
                s.__init__()

            else:
                print('Invalid choice')


s = Bank_Account()
s.choice()
