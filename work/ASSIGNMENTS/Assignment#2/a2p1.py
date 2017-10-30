import math
import random


"""
high_school_eqsolver: This function has three parameters representing three real numbers for the coefficients of the
quadratic equation ax 2 + bx + c = 0. 

The function displays/prints the equation frist and then prints its solutions.
The function must display correct and meaningful solutions given any three real numbers for coefficients a, b and
c. See examples in Section 4 to understand what that means. Please consider the examples (and the video) to be a
part of the function/program specifications that must be followed.
Note that to solve this problem, you do not need to use Python’s complex numbers.
"""

def primary_school_quiz(flag, n):
    # Your code for primary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    from random import randint
    total = 0
    if flag == 0:
        
        for i in range(n):
            print("Question ", i+1)
            n1 = randint(1,9)
            n2 = randint(1,9)
            answer = int(n1 - n2)
            user_answer = int(input("Whats the result of %s - %s"%(n1,n2)))

            if user_answer == answer:
                total = total + 1

    elif flag == 1:
        for i in range(n):
            print("Question", i+1)
            n1 = randint(1,9)
            n2 = randint(1,9)
            answer = int(n1**n2)
            user_answer = int(input("Whats the result of %s^%s? "%(n1,n2)))

            if user_answer == answer:
                total = total + 1
    else:
        return
    
    return total

# print(primary_school_quiz(1, 3))

def high_school_eqsolver(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    from math import sqrt
    if b**2 < 4*a*c:
        print("The quadratic equation %sx^2 + %sx + %s = 0"%(a,b,c))
        print("has the following complex roots")
        #TODO figure out how to do the complex roots stuff
        r = -b / 2*a
        r1c = sqrt(abs(b**2 - 4*a*c)) / 2*a
        r2c = sqrt(abs(b**2 - 4*a*c)) / 2*a
        print("%s + i %s and %s - i %s"%(r,r1c, r, r2c))
    elif b**2 == -4*a*c:
        print("The quadratic equation %sx^2 + %sx + %s = 0"%(a,b,c))
        print("Has one real root")
        r = -b / 2*a
        print(r)
    else:
        r1 = (-b + sqrt(b**2 - 4*a*c)) / 2*a
        r2 = (-b - sqrt(b**2 - 4*a*c)) / 2*a

        print("The quadratic equation %sx^2 + %sx + %s = 0"%(a,b,c))
        print("Has the following real roots")
        print(r1, "and", r2)



# main

# your code for the welcome tmessage goes here
def box_generator(text):
    print("*"*(len(text)+10))
    print("*" + " "*(len(text)+8) + "*")
    print("*  __" + text + "__  *")
    print("*" + " "*(len(text)+8) + "*")
    print("*"*(len(text)+10))

box_generator("Welcome to my math quiz-generator / equation-solver")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n ")

if status=='1':
    # your code goes here
    box_generator("%s, welcome to my quiz-generator for primary school students."%name)

    flag = int(input("Vida what would you like to practice? Enter\n0 for subtraction\n1 for exponentiation "))
    n = int(input("How many practice questions would you like to do? "))
    primary_school_quiz(flag, n)

elif status=='2':
    
    # your code for welcome message

    box_generator("quadratic equation, a·x^2 + b·x + c= 0, solver for %s"%name)
    
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here
        question = question.lower()
        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
            a = int(input("Enter a number the coefficient a: "))
            b = int(input("Enter a number the coefficient b: "))
            c = int(input("Enter a number the coefficient c: "))
            high_school_eqsolver(a,b,c)
else:
    # your code goes here
    pass

print("Good bye "+name+"!")

