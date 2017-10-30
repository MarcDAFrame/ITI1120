def mess(s):
    s = s.replace(' ', '_')
    test = ""
    for i in s:#["r", 's', 't', 'v', 'w', 'y', 'z', "R", 'S', 'T', 'V', 'W', 'Y', 'Z']:
        if i in ["r", 's', 't', 'v', 'w', 'y', 'z', "R", 'S', 'T', 'V', 'W', 'Y', 'Z']:
            test = test + i.upper()
        else:
            test = test + i  
        # s= s.replace(i, i.upper())
        
    return s

# print(mess("Test this is really coolz"))

def pyramid1(n):
    for i in range(n):
        print("*"*i)

def pyramid2(n):
    for i in range(1, n, 2):
        print(" "*(((n-i)//2)+1) + "*"*i + " "*((n-i)//2))

def find_divisors():
    n = int(input("what number do you want to check? "))
    for i in range(1, n):
        if n%i == 0:
            print(i)

def is_prime(n):
    if n > 2:
        for i in range(2, n):
            if n%i == 0:
                return False
    else:
        return False
    return True

def primes_in(n):
    for i in range(n):
        if is_prime(i):
            print(i)

# primes_in(50)
# find_divisors()
# pyramid2(10)

def task3():
    s = '"It was the best of times, it was the worst of times;\nit was the age of wisdom, it was the age of foolishness;\nit was the epoch of belief, it was the epoch of incredulity;\nit was ..."'
    newS = s.replace(',', ' ').replace('.', ' ').replace('\n', ' ').replace(';', ' ')
    print(newS)#a
    newS = s.strip()
    print(newS)#b
    print(newS.lower())#c
    print(newS.lower().count("it was"))#d
    print(newS.replace("was", "is"))#e


def task2():
    aha = "abcdefgh"
    print(aha[0:4])
    print(aha[3:6])
    print(aha[7])
    print(aha[5:-1])
    print(aha[3:])
    print(aha[0] + aha[3] + aha[6])
    print(aha[1] + aha[4])

def task1():
    s1 = "good"
    s2 = "bad"
    s3 = "silly"
    print(s3[2:4])
    print(s1+s2+s3)
    print(s1 + " " + s2 + " " + s3)
    print(s3*10)
    print(len(s1+s2+s3))

task2()



