from task5 import primes


if __name__ == "__main__":
    l = itertools.takewhile(lambda x : x <= 17, primes())
    print(list(l)) # [2, 3, 5, 7, 11, 13, 17]
