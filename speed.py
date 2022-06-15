# Q27. Write a function for checking the speed of drivers. This function
# should have one parameter: speed.

def my_func(speed):
    point=0
    if speed>70:
        speed=speed-70
        div=speed//5
        if div>12:
            return "license suspended"
        else:
            return "points=",div
    else:
        return "ok" 
speed=int(input("enter speed: "))
print(my_func(speed))  
