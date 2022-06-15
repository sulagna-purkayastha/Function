# generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
# generate_range(1, 10, 3) # should return list of [1,4,7,10]
# generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
# generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]

def generate_range(min,max,step):
    list=[]
    min=min   
    while min<=max:
        list.append(min)
        min=min+step
    return list
min=int(input("enter min no: "))
max=int(input("enter max no: "))
step=int(input("enter step no: "))
print(generate_range(min,max,step))