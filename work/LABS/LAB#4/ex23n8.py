def is_divisible(n,m):
     '''(int, int)->bool
     returns True if n is divisible by n, and False otherwise.'''
     return n%m==0

def is_divisible23n8(n):
     '''(int)->bool
     returns string "yes" if n is divisible by 2 or 3 but not 8, and "no" otherwise.'''
     for i in range(n, 0, -1):
        if ( (is_divisible(i,2) or is_divisible(i,3)) and not(is_divisible(i,8))):
            return True
        else:
            return False

def print_all_23n8(num):
    for i in range(num, 0, -1):
        if is_divisible23n8(i):
            print(i)

print_all_23n8(20)