from task5 import primes


if __name__ == "__main__":
    for i in primes():
        print(i)
        if(i > 19):
            break
