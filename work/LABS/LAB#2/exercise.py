def repeater(s1, s2, n):
    return "_" + (s1 + s2)*n + "_"

#print(repeater('T', 'I_I', 5))

def roots(a, b, c):
    import math
    sqr = math.sqrt(b**2 - 4*a*c)
    print("the quadratic equation with coefficients a=%s, b=%s, c=%s"%(a,b,c), "has the following solutions")
    print( (-b + sqr)/(2*a), "and",(-b - sqr) / (2*a) ) 

# roots(1, 0, -4)

def real_roots(a, b, c):
    return b**2 > 4*a*c

# print(real_roots(1, 0, -4))

def reverse(x):
    return (x%10)*10 + (x // 10)

print(reverse(36))