# Q17. Write a function to tell user if he/she is able to vote or not.

def my_func(age):
    if age>=18:
        return age,"is able to vote"
    else:
        return age,"is not able to vote"
age=int(input("enter age: "))
print(my_func(age))