def is_perfect(n):
    total = 0
    for i in range(1, n-1):
        if n % i == 0:
            total = total + i

    if total == n:
        return True
    return False

# print(is_perfect(6))
"""
for i in range(2, 35000000, 2):
    if is_perfect(i):
        print(i)
"""



def arithmatic(li):
    if len(li) == 1:
        return True

    d = abs(li[0] - li[1])
    counter = li[0]
    for i in li:
        if i != counter:
            return False
        counter = counter + d
    return True

def is_sorted(li):
    if len(li) == 1:
        return True

    d = abs(li[0] - li[1])
    counter = li[0]
    for i in li:
        if i != counter:
            return False
        counter = counter + d
    return True


# print(is_sorted([-7, -5, -3, -1]))