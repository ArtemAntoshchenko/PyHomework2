# 1)
def sum(int1,int2,int3,in4=4,int5=5):
    return print(int1+int2+int3+in4+int5)
sum(1,2,3)

# 2)
def even(int):
    return print(int%2==0)
even(1)
even(2)

# 3)
def outer(func,list):
    for i in list:
        print(func(i))
def inner(i):
    return 1+i
list1=[1,5,3]
outer(inner,list1)

# 4)