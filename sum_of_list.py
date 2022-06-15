# Write a Python function to sum all the numbers in a list.
# List : (8, 2, 3, 0, 7)Output : 20.

def my_func(list):
    i=0
    sum=0
    while i<len(list):
        a=list[i]
        sum=sum+int(a)
        i=i+1
    print(sum)
list=[8,2,3,0,7]
my_func(list)