class Account:
    def init(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, count):
        self.balance += count

    def withdraw(self, count):
        if count > self.balance:
            print('You do not have enough')
        else:
            self.balance -= count

