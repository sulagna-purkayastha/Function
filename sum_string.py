# Q10.Create a function that takes 2 positive integers in form of a
# string as an input, and outputs the sum (also as a string):
# "4", "5" --> "9"
# "34", "5" --> "39"
# If either input is an empty string, consider it as zero.

def my_func(a,b):
    if a!=0 and b!=0:
        sum=int(a)+int(b)
        sum=str(sum)
        return sum
    else:
        return 0
a=input("enter no")
b=input("enter no")
print(my_func(a,b))