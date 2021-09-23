from task4 import BankCard

if __name__ == "__main__":
    a = BankCard(0)
    try:
        a(0)
        print(a)
    except ValueError:
        pass