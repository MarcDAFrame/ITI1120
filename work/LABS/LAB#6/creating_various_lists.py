"""
1.Create	a	list	a	(i.e	a	list	referred	to	by	variable	a)	of	length	n	filled	with	zeros
2.Create	a	list	b	of	length	n	filled	with	random	integers	between	1	and	100
3.Create	a		variable	c	that	is	an	alias	of	b
4.Set	first	half	of	the	elements	of	c	to	zero,	and	then	print	both	b	and	c
5.Copy	list	b	into	a	list	d
6.Create	a	new	list	e	that	has	every	2 nd element	of	b
"""

n=int(input("Enter a positive even integer for the size of the list?" ))

#1
a = [0]*n
a1 = [0]
i=0
while i < n-1:
    a1 = a1+[0]
    i = i + 1
print(a, a1)
#2
from random import randint
# b = [(lambda: randint(0, 100))]*n
b = [randint(0,100) for x in range(n)]

b1 = [0]
i=0
while i < n-1:
    b1 = b1+[randint(0,100)]
    i = i + 1
print(b, b1)
#3
c = b[:]
c1 = []
i=0
while i<len(b):
    c1 = c1+[b[i]]
    i = i + 1

print(c, c1)
#4
c = ([0]*(len(c)//2)) + (c[len(c)//2:])
c1 = []
i=0
while i < len(c):
    if i < len(c)//2:
        c1 = c1 + [0]
    else:
        c1 = c1 + [c[i]]
    i = i + 1
print(c, c1)
#5
d = b[:]
d1 = []
i=0
while i<len(b):
    d1 = d1+[b[i]]
    i = i + 1

print(d, d1)
#6
e = b[::2]
e1 = []
i = 0
while i < len(b):
    if i % 2 == 0:
        e1 = e1 + [b[i]]
    i = i + 1
print(e, e1)