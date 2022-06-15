# Q38. Your task is to create function is Divided By (or is_divide_by)
# to check if an integer number is divisible by each out of two arguments.

# A few cases:
# (-12, 2, -6) -> true(-12, 2, -5) -> false
# (45, 1, 6) -> false
# (45, 5, 15) -> true
# (4, 1, 4) -> true
# (15, -5, 3) -> true



def is_divided_by(*divident):
    divisor= int(input("enter divisor: "))
    count=0
    count_1=0
    i=1
    j=0
    while j<len(divident):
        a=divident[j]
        while i<3:
            if divisor % int(a)==0:
                count=count+1
            # else:
            #     count_1=count_1+1
            i=i+1
        j=j+1
    if count>1:
        print ("True")
    else:
        print ("False")
is_divided_by(45,5,15)