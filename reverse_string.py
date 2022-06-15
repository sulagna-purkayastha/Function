# Q4.Write a Python program to reverse a string.
# Sample String : "1234abcd" # Output : "dcba4321".

def my_func(reverse):
    i=-1
    a=0-len(reverse)
    while i>=a:
        print(reverse[i],end="")
        i=i-1
reverse="1234abcd"
my_func(reverse)