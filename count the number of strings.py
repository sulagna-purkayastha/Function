# Write a Python program to count the number of strings where the string length is 2
# the first and last characters are the same from a given list of strings.
# ist=['abc', 'xyz', 'aba', '1221'] # result= 2.

def my_func(list):
    i=0
    sum=0
    while i<len(list):
        if len(list[i])>1:
            if list[i][0]==list[i][-1]:
                sum=sum+1
        i=i+1
    print(sum)
list=['abc', 'xyz', 'abc', '1221', 'aba']
my_func(list)