#Q7.Write function bmi that calculates body mass index
#(bmi = weight / height2).

def func(weight,height):
    bmi=weight//height
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
weight=float(input("enter weight"))
height=float(input("enter height"))
print(func(weight,height))