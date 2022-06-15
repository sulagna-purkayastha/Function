# Q14.Write a function to check if a number is prime or not.

def my_func(num):
    if i>1:
        i=1
        while i<=num//2:
            if num%i==0:
                print(num,"not a prime")
                break
            i=i+1
        else:
            print(num,"prime")
    else:
        print(i,"is a natural no") 
num=int(input("enter no"))
my_func(num)

# i=2
# while i<=a//2:
#     if a%i==0 or a==1:
#         print("not a prime no")
#         break
#     i=i+1
# else:
#     print("prime no")