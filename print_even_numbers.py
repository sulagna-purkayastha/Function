# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].



def my_func(list):
    i=0
    new=[]
    while i<len(list):
        a=list[i]
        if a%2==0:
            new.append(a)
        i=i+1
    print(new)
list= [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_func(list)           