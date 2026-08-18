#check whether a number is prime
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
num = int(input("Enter a number: "))
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")

#*args
def largest(*args):
     return max(args)
print("maximum",largest(10,20,30,40))

#**kwargs
def info(**kwargs):
    for key, value in kwargs.items():
        print(key , ":" , value)
info(name = "Ritika" , branch = "Cse")

#challange
def func(lst):
    maximum = max(lst)
    minimum = min(lst)
    average = sum(lst) / len(lst)
    add = sum(lst)
    return maximum , minimum , average ,add
print(func([30,15,20,72]))