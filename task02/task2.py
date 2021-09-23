def is_palindrome(x):
    if x<0:
        return "NO"
    reDefine=x;
    list=[]
    while reDefine> 10:
        aparm=int(reDefine%10);
        list.append(aparm);
        reDefine=reDefine/10
    list.append(int(reDefine))
    if list==list[::-1]:
        return "YES"
    else:
        return "NO"

