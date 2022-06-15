# Q13.Write a function to check if a number is even or not.


def my_func(num):
    if num%2==0:
        return "even no"
    else:
        return "not even no"
num=int(input("enter num: "))
print(my_func(num))