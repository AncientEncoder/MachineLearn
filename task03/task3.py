def longestCommonPrefix(x) :
    result = ''
    for j in range(len(x)):
        x[j]=x[j].strip()
    for i in zip(*x):
        if len(set(i)) == 1:
            result += i[0]
        else:
            break
    return result