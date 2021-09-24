def hello(x=""):
    if x == "":
        x = "Hello!"
    elif x[-1]=='!':
        x = "Hello," + x
    else:
        x="Hello, " + x+"!"
    return x
