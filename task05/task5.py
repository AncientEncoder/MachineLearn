def primes():
    ditionarysD = {}
    num = 2
    while num <= 1000:
        if num not in ditionarysD:
            yield num
            ditionarysD[num*num] = [num]
        else:
            for p in ditionarysD[num]:
                ditionarysD.setdefault(p + num, []).append(p)
            del ditionarysD[num]
        num += 1

