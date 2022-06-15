# Q16.Print multiplication table of 12 using function.



def my_func(num):
    i=1
    while i<=10:
        table= num*i
        i=i+1
        print(table)
num=int(input("enter no: "))
my_func(num)
num_1=int(input("enter no"))
my_func(num_1)