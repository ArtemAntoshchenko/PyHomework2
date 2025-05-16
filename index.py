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
count=0
if (True):
    temp=10
    count+=temp
    print(temp)
print(count)
print(temp)

def local():
    temp=5
    temp+=count
    return print(temp)
local()
print(temp)

# 5)
def count1():
    x=0
    def counter():
        nonlocal x
        x+=1
        print (x)
    return counter
closure=count1()
closure()
closure()

# 6)
def count1(y):
    x=0
    def counter(y):
        nonlocal x
        x+=y
        print (x)
    return counter
closure=count1(2)
closure(3)
closure(4)
