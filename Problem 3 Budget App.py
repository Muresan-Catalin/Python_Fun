class Category:
    ledger = list()
    total = 0
    name = ""

    def __init__(self, nam):
        self.name = nam

    def check_funds(self, ammount):
        return self.total > ammount

    def deposit(self, ammount, description):
        obj = dict()
        ammount = float("{0:.2f}".format(ammount))
        obj[description] = ammount
        self.ledger.append(obj)
        self.total += ammount
        #print(self.ledger, self.total)

    def withdraw(self, ammount, description):
        if self.check_funds(ammount):
            obj = dict()
            ammount = float("{0:.2f}".format(ammount))
            obj[description] = -ammount
            self.ledger.append(obj)
            self.total -= ammount
            #print(self.ledger, self.total)
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, ammount, budget):
        newText = "Transfer to "
        newText += budget.name
        self.withdraw(ammount, newText)

    def __repr__(self):
        #print stars and name
        a = (30 - len(self.name)) / 2
        if len(self.name) % 2 == 1:
            x = int(a)
            y = x + 1
        else:
            x = a
            y = a

        i = 1
        while i <= x:
            print('*', end="")
            i += 1
        print(self.name, end="")
        i = 1
        while i <= y:
            print('*', end="")
            i += 1
        print('\n')

        #print ledger
        for i in self.ledger:
            for j in i:
                key = str(j)
                value = str(i[j])
                print(f"{key[:23]:<23}{value:>7}")

        totalTxt = "Total " + str(self.total)
        return totalTxt

food = Category("Foods")
food.deposit(100, 'casa')
food.deposit(350, 'sticle')
food.withdraw(50, 'dopuri')
print(food)

periferice = Category("Periferice")
periferice.deposit(500, 'tastatura')
periferice.deposit(250, 'mouse')
periferice.withdraw(350, 'casti')
periferice.transfer(50.234, food)
print(periferice)
