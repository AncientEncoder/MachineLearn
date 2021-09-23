class BankCard:
    def __init__(self, total_sum):
        self.total_sum = total_sum


    def __call__(self, cost):
        if cost>self.total_sum :
            print("Not enough money to spent {0} dollars.".format(cost))
            raise ValueError


    @property
    def balance(self):
        if self.total_sum<1 :
            print("Not enough money to learn the balance.")
            raise ValueError
        self.total_sum-=1
        return self.total_sum


    def put(self,moneyIn):
        self.total_sum+=moneyIn
        print("You put {0} dollars. {1} dollars are left.".format(moneyIn,self.total_sum))


    def __repr__(self):
        return "To learn the balance you should put the money on the card, spent some money or get the bank data.The last procedure is not free and costs 1 dollar."