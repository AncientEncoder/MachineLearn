def process(l):
    return sorted(set(i*i for i in sum (l,[])))[::-1]
