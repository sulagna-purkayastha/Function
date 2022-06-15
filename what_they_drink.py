# Kids drink toddy.# Teens drink coke.# Young adults drink beer.
# Adults drink whisky,# Make a function that receive age
# and return what they drink.

def drink_what(age):
    if age<14:
        return "toddy"
    elif age<18:
        return "coke"
    elif age<21:
        return "beer"
    else:
        return "whisky"
age= int(input("enter age: "))
print(drink_what(age))