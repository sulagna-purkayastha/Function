# Q12.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

def my_func(num):
    i=-1
    while i<int(num[i]):
        a=num[i]
        if a==0:
           new= num//0
           print(new)
        i=i+1
    else:
        print(num)
    # print(new)
num=input("enter no: ")
my_func(num)