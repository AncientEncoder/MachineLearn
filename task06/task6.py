def check(s, file):
    dArr = dict()
    s=s.lower()
    list=s.split(" ")
    for keyGen in list:
        if dArr.get(keyGen)==None:
            dArr[keyGen]=1
        else:
            dArr[keyGen]+=1
    with open(file, 'w') as fOut:
        for keyGen in sorted(dArr):
            fOut.write(keyGen)
            fOut.write(' ')
            fOut.write(str(dArr[keyGen]))
            fOut.write('\n')
