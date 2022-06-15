# Q8.Write a Python function that accepts a string and calculate the
# number of upper case letters and lower case letters.

def char(str):
    i=0
    sum_upper=0
    sum_lower=0
    while i<len(str):
        a=str[i]
        if a>="A" and a<="Z":
            sum_upper=sum_upper+1
        if a>="a" and a<="z":
            sum_lower=sum_lower+1
        i=i+1
    print("upper case in charecter=",sum_upper)
    print("lower case in charecter=",sum_lower)
str=input("enter any character")
char(str)
