def longestCommonPrefix(x) ->str :
    result = ''
    for i in zip(*x):
        if len(set(i)) == 1:
            result += i[0]
        else:
            break
    return result