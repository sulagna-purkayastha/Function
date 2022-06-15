# Q27. Write a function for checking the speed of drivers. This function
# should have one parameter: speed.




def my_func(speed):
    point=0
    if speed<70:
        return "ok"
    elif speed>=70:
        i=1
        count=0
        point=0
        while i<=speed:
            count=count+1
            if count==5:
                point= point+1
                return "point =",point
            i=i+1
    if point>12:
            return "License suspended" 
speed=int(input("enter speed: "))
print(my_func(speed))   

        
        
