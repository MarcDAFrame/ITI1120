"""
Assignment #2
Marc Frame
Oct 15th 2017

Prof. Vida Dujmovic
"""

###################################################################
# Question 1
###################################################################
def min_enclosing_rectangle(radius, x, y):
    # print(radius, x, y)
    if radius > 0 and x > 0 and y > 0:
        return (x-radius, y-radius)

###################################################################
# Question 2
###################################################################
def series_sum():
    n = int(input("Please enter a non-negative integer: "))
    total = 1000
    if n >= 0:
        for i in range(1, n):
            
            total = total + (1/i**2)
        return total

###################################################################
# Question 3
###################################################################
def pell(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif (n <= 2):
        return n
    return 2 * pell(n - 1) + pell(n - 2)

###################################################################
# Question 4
###################################################################
def countMembers(s):
    total = 0
    for c in s:
        if c in "efghijFGHIJKLMNOPQRSTUVWX23456!,\\":
            total = total + 1
    
    return total

###################################################################
# Question 5
###################################################################
def casual_numbers(s):
    s = s.replace(',', '')
    try:
        return int(s)
    except:
        return None

###################################################################
# Question 6
###################################################################
def alienNumbers(s):
    total = 0
    for x,char in enumerate("Ty!aNU"): 
        total = total + [1024, 598, 121, 42, 6, 1][x]*s.count(char)
    return total


###################################################################
# Question 7
###################################################################
def encrypt(s):
    s = s[::-1]
    new_string = ""
    for i in range(len(s)//2):
        new_string = new_string + s[i] + s[-i-1]
    
    return new_string

###################################################################
# Question 8
###################################################################
def alienNumbersAgain(s):
    total = 0
    for x,char in enumerate("Ty!aNU"):
        count = 0
        for i in s:
            if i == char:
                count = count + 1
        total = total + [1024, 598, 121, 42, 6, 1][x]*count
    return total

###################################################################
# Question 9
###################################################################
def oPify(s):
    acumulator = s[0]
    for i in range(len(s)-1):
        pair = s[i] + s[i+1]

        if pair.isalpha():
            if pair[0].isupper():
                acumulator = acumulator + "O"
            else:
                 acumulator = acumulator + "o"
            if pair[1].isupper():
                acumulator = acumulator + "P" + pair[1]
            else:
                acumulator = acumulator + "p" + pair[1]
        else:
            acumulator = acumulator + pair[1]
    return acumulator

###################################################################
# Question 10
###################################################################
def nonrepetitive(s):
    words = []
    for i in range(len(s)):
        for j in range(i, (len(s)+2)//2):
            words.append((s[i:i+j], i, i+j))
    for word in words:
        for word2 in words:
            if word[0] == word2[0] and word != word2:
                return False
    return True

print(nonrepetitive(''))



