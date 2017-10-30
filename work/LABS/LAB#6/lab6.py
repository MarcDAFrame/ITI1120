def add():
    while True:
        x = float(input("input a number"))
        y = float(input("input a number"))
        
        print(x+y)
        if input("do you want to continue (yes or no)") != 'yes':
            break

def first_neg(li):
    i = 0
    while i < len(li):
        if li[i] < 0:
            return i
        i = i + 1

    return None

# add()
# print(first_neg([1,-2,-3]))

def sum_5_consecutive(li):
    i = 0
    j = 0
    count = 1
    while i < len(li):
        total = 0
        if len(li) - i < 5:
            return False
        while j < 5:
            total = total + li[i+j]
            j = j + 1
        if total == 0:
            return True
            
        i = i + 1
    return False

# print(sum_5_consecutive([2, 1, -3, -3, -3, 2, 7, 4, -6]))
def fib(n):
    a = [1,1]
    i = 2
    while i < n:
        a = a + [a[i-2] + a[i-1]]
        i = i + 1

    return a

# print(fib(10))

def inner_product(lia, lib):
    i=0
    total = 0
    while i < len(lia):
        total =  total + lia[i]*lib[i]
        i = i + 1
    return total

print(inner_product([2,3,4], [1,0,2]))
