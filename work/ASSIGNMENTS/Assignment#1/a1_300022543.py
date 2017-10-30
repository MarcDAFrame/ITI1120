"""
Assignment #1
Marc Frame
Sept. 20th 2017

Prof. Vida Dujmovic
"""

###################################################################
# Question 1
###################################################################
def mh2kh(s):
    """(number)->number
    Preconditions: a non negative number is provided
    Purpose: converts mph to kmh
    returns a converted value from mph to kmh by multiplying by a constant
    """
    return s*1.60934

###################################################################
# Question 2
###################################################################
def pythagorean_pair(a,b):
    """(number, number) -> boolean
    Preconditions: two non negative numbers are provided for sides of the triangle
    Purpose: finds the value for c using pythagorean theorem and then tests to see if it is an integer value
    returns a boolean on whether length c is an integer value or not
    """
    import math
    c = math.sqrt(a**2 + b**2)
    return c == int(c)

###################################################################
# Question 3
###################################################################
def in_out(xs,ys,side):
    """(number, number, number) -> boolean
    Preconditions: three non negative numbers
    Purpose: bounding box creation and detection on whether an inputted value is within the bounding box
    returns a boolean True if the value is in the bounding box else False
    """
    x = float(input("x position: "))
    y = float(input("y position: "))

    return x>=xs and y>=ys and x<=xs+side and y<=ys+side

###################################################################
# Question 4
###################################################################
def safe(n):
    """(number)->boolean
    Preconditions: a number with less then or equal to 2 digits
    Purpose: to determine if a number is 'safe' or not
    returns a boolean if it doesn't contain 9 with, if it is not divisible by 9 
    """
    return n % 9 != 0 and str(n)[0] != '9' and str(n)[1] != '9'

###################################################################
# Question 5
###################################################################
def quote_maker(quote, name, year):
    """(string, string, string) -> string
    Preconditions: strings that will work with the sentence structure are provided
    Purpose to create a string to display a quote
    returns a string that includes year, quote and creator of quote in an eloquent sentence
    """
    final_str = "in " + str(year) + ", a person called " + str(name) + " said " + str(quote)
    return final_str

###################################################################
# Question 6
###################################################################
def quote_displayer():
    """(None) -> string
    input: 
        quote | str | ex. "don't quote me on this"
        name  | str | ex. Marc Frame
        year  | str | ex. 2017
    preconditions: input is provided
    Purpose: to get input and print a string
    returns None
    """
    quote = input("What is your quote? ")
    name = input("Who said the quote? ")
    year = input("When did " + name + " say '" + quote + "' ")

    print(quote_maker(quote, name, year))

###################################################################
# Question 7
###################################################################
def rps_winner():
    """(None) -> None
    Preconditions: input is provided
    Purpose: to compare rock paper scissors games between two players and determine a winner or if there is a draw
    returns None
    """
    player1 = input("[PLAYER ONE] choose (rock, paper, scissors): ")
    player2 = input("[PLAYER TWO] choose (rock, paper, scissors): ")

    result = (player1 == 'rock' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock')
    tie_result = not (player1 == player2)

    print("[PLAYER ONE] WINS! that is " + str(result))
    print("             It is a tie! that is not " + str(tie_result))

###################################################################
# Question 8
###################################################################
def fun(x):
    """(number) -> number
    Preconditions: a value greater than -3 must be provided
    Purpose: to determine a value for y given x
    returns a value for y based off of a given equation
    """
    import math
    return (math.log(x + 3)/math.log(10))/4

###################################################################
# Question 9
###################################################################
def ascii_name_plaque(name):
    """(string) -> None
    Preconditions: a string for a name must be provided
    Purpose: to print a named surrounded by a plaque
    returns None
    """
    print("*"*(len(name)+8))
    print("*" + " "*(len(name)+6) + "*")
    print("* " + "__" + name + "__" + " *")
    print("*" + " "*(len(name)+6) + "*")
    print("*"*(len(name)+8))

###################################################################
# Question 10
###################################################################
def draw_bike():
    """(None) -> None
    Preconditions: program must be run
    Purpose: to draw a bike with the Turtle TK
    returns None
    """
    import turtle
    import time
    def move(x, y):
        t.penup()
        t.setx(x)
        t.sety(y)
        t.pendown()
    
    
    # t.speed(100)
    s=turtle.Screen()
    t=turtle.Turtle()
    
    t.pensize(2)
    #wheel1
    move(-200, -230)
    t.circle(80)
    move(-200, -150)

    #body
    t.pensize(4)
    t.color('blue')
    t.goto(-100,0)
    t.goto(100, 0)
    t.goto(125, -150)
    move(-200, -150)
    t.goto(-50, -150)
    t.goto(100, 0)

    #handle bars
    t.pensize(5)
    t.color('grey')
    move(100, 0)
    t.goto(100, 10)
    t.goto(120, 20)
    
    #seat
    t.pensize(6)
    t.color('brown')
    move(-80, 0)
    t.goto(-80, 10)
    t.goto(-70, 10)
    t.goto(-100, 10)

    #pedals
    t.pensize(4)
    t.color('grey')
    move(-50, -170)
    t.circle(20)
    move(-55, -170)
    t.goto(-60, -185)
    move(-50, -130)
    t.goto(-45, -115)
    

    #wheel 2
    t.pensize(2)
    t.color('black')
    move(125, -230)
    t.circle(80)

    t.pensize(1)
    #spokes
    for i in range(10):
        move(125, -150)
        t.setheading((360/10 * i))
        t.forward(80)
    
    #spokes
    for i in range(10):
        move(-200, -150)
        t.setheading((360/10 * i))
        t.forward(80)
        

    #delay the app closing
    move(1000, 1000)
    time.sleep(5)

###################################################################
# Question 11
###################################################################
def alogical(n):
    """(number) -> number
    Preconditions: number provided
    Purpose: to find out how many times you have to divide a number by 2 in order for it to be less than one
    returns an int
    """
    import math
    return math.ceil(math.log(n)/math.log(2))

###################################################################
# Question 12
###################################################################
def time_format(h, m):
    """(number, number) -> string
    Preconditions: hours and minutes provided
    Purpose: to convert hour and minute values to an eloquent word clock
    returns a string with time as a string 
    """
    h = h%24
    m = int(5 * round(float(m)/5))    

    if m == 0:
        output = str(h) + " o'clock"   
    elif m == 60:
        output = str((h+1)%24) + " o'clock"
    elif m < 30:
        output = str(m) + " minutes past " + str(h)
    elif m > 30:
        output = str(m) + " minutes to " + str((h+1)%24)
    elif m == 30:
        output = "half past " + str(h)

    return output 

###################################################################
# Question 13
###################################################################
def cad_cashier(price, payment):
    """(number, number) -> number
    Preconditions: payment >= price, price and payment are non-negative
    Purpose: to deterine change due to the nearest nickle 
    Returns: change due to the nearest nickle
    """
    price = int(5 * round(float(price * 100)/5))/100
    return round((payment-price)*100)/100

###################################################################
# Question 14
###################################################################
def min_CAD_coins(price, payment):
    """(number,number)->(number,number,number,number,number)
    Preconditions: payment >= price, price and payment are non-negative
    Purpose: to determine change due and types and quantity of change due
    Returns: change due including type of coin and quantity of change due
    """
    change_due = cad_cashier(price, payment)
    #(t,l,q,d,n) 
    t = int(change_due // 2)
    change_due = change_due % 2
    l = int(change_due // 1)
    change_due = change_due % 1
    q = int(change_due // 0.25)
    change_due = change_due % 0.25
    d = int(change_due // 0.10)
    change_due = change_due % 0.10
    n = int(change_due // 0.05)
    change_due = change_due % 0.05

    return (t, l, q, d, n)
