
value = 20

def sample():
    value = 30
    print(value)
    value =value + 1
    print(value)



print(value)
sample()

def globalvar():

    s=value+1
    print("\n"+str(s))

globalvar()