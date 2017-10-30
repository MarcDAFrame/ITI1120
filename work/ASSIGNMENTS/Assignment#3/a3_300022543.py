import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    print("Shuffling the deck...")
    for i in range(len(deck)):
        swap = random.randrange(len(deck) - 1)
        swap += swap >= i
        deck[i], deck[swap] = deck[swap], deck[i]
    
    return deck


def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE
    for index in range(1, len(original_board)+1):
        if index in discovered or index == p1 or index == p2:
            if index < 10:
                print(original_board[index-1], end='  ')
            else:
                print(original_board[index-1], end='    ')

        else:
            if index < 10:
                print('*', end='  ')
            else:
                print('*', end='    ')
    print()
    for index in range(1, len(original_board)+1):
        if index < 10:
            print(index, end='  ')
        else:
            print(index, end='   ')

    
    print()
    print()

def clear_board():
    '''None->None
    prints out a lot of lines in order to clear the console screen
    '''
    print('\n'*50)

#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    checked = []
    #had to make a copy of the list cause it was editing the list (as we learnt in lecture #9)
    old_l = l[:]
    x = 0
    for item in l:
        #iterates through list
        a = old_l.pop(x)  
        #pops the item of the list at the index of that list (counted by x)
        if item in old_l and item not in checked and item != "*":#
            #if item is not in the list or item appears more than twice it adds it to the array twice
            playable_board.append(item)
            playable_board.append(item)


        old_l = [None] + old_l
        #adds a none to the beginning of the list to preserve position and length of list
        if item in checked:
            #if the item is in checked then we remove it from the checked
            checked.remove(item)
        else:
            #if it is not in checked then we add it to it
            checked.append(item)
        #if there is an even amount of items in the list this allows for them to be added to the deck

        x += 1
    return playable_board


def is_rigorous(l):
    '''list of str->bool
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''
    checked = []
    #had to make a copy of the list cause it was editing the list (as we learnt in lecture #9)
    old_l = l[:]
    for x,item in enumerate(l):
        old_l.pop(x)
        #removes item from list to check if there is another occurance of it, if there isn't it returns False
        if item not in old_l or item in checked:
            #if item is not in the list or item appears more than twice return False
            return False
        
        checked.append(item)

    return True
    # YOUR CODE GOES HERE
 
                
        

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the funciton that plays the game
    # YOUR CODE GOES HERE
    total_guesses = 0
    #paired is a list of all the indexs of paired pieces if
    paired = []
    while True:
        print_revealed(paired, 0, 0, board)

        while True:
            print()
            #this loop goes until the user provides proper
            print("Enter two distinct positions on the board that you want revealed.")
            print("i.e two integers in the range [1, %s]"%len(board))
            pos1 = int(input("Enter position 1: "))
            pos2 = int(input("Enter position 2: "))
            

            if pos1 == pos2:
                #if it is the same print that they are the same
                print("You chose the same positions.")
                if pos1 < 1 or pos1 > len(board) or pos2 < 1 or pos2 > len(board):
                    #if it is not within the interval
                    print("You chose a position outside of the interval [1, %s]"%len(board))
                if pos1 in paired or pos2 in paired:
                    #if the position has already been paired
                    print("One or both of your chosen positions has already been paired.")

                print("Please try again. This guess did not count. You current number of guesses is  %s."%total_guesses)

            elif pos1 < 1 or pos1 > len(board) or pos2 < 1 or pos2 > len(board):
                #if it is not within the interval
                print("You chose a position outside of the interval [1, %s]"%len(board))
                if pos1 in paired or pos2 in paired:
                    #if the position has already been paired
                    print("One or both of your chosen positions has already been paired.")
                
                print("Please try again. This guess did not count. You current number of guesses is  %s."%total_guesses)
            elif pos1 in paired or pos2 in paired:
                #if the position has already been paired
                print("One or both of your chosen positions has already been paired.")
                print("Please try again. This guess did not count. You current number of guesses is  %s."%total_guesses)
            else:
                #if it meets all these conditions then it passes
                break
        
        total_guesses = total_guesses + 1
        if board[pos1-1] == board[pos2-1]:
            paired.append(pos1)
            paired.append(pos2)

        print_revealed(paired, pos1, pos2, board)
        wait_for_player()
        clear_board()
        if len(paired) == len(board):
            break
    
    if total_guesses - len(board)//2 == 0:
        print('Congratulations! You completed the game with %s guesses. That is the best possible score.'%total_guesses)
    else:
        print('Congratulations! You completed the game with %s guesses. That is %s more than the best possible.'%(total_guesses, total_guesses - len(board)//2))




#main
print("******************************************")
print("*                                        *")
print("*  __Welcome to my Concentration game__  *")
print("*                                        *")
print("******************************************") 
print('\n'*2)
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE
print("Would you like (enter 1 or 2 to indicate your choice):")
print("(1) me to generate a rigorous deck of cards for you")
print("(2) or, would you like me to read a deck from a file?")
while True:
    first_choice = input()
    if first_choice == '1' or first_choice == '2':
        break
    else:
        print(first_choice + " is not existing option. Please try again. Enter 1 or 2 to indicate your choice")

# YOUR CODE FOR OPTION 1 GOES HERE
# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)
if first_choice == '1':
    print("You chose to have a rigorous deck generated for you")
    while True:
        print()
        print("How many cards do you want to play with?")
        deck_size = int(input("Enter an even number between 0 and 52: "))
        if deck_size % 2 == 0 and deck_size >= 2 and deck_size <= 52:
            #checks if its within the interval [2, 52] and is an even number
            break
        
    unshuffled_deck = create_board(deck_size)
    deck = shuffle_deck(unshuffled_deck)
    wait_for_player()
    clear_board()
    play_game(deck)

# YOUR CODE FOR OPTION 2 GOES HERE
# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
#
if first_choice == '2':
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")

    file=file.strip()
    board=read_raw_board(file)
    deck = clean_up_board(board)

    if not is_rigorous(board):
        if len(deck) >= 10:
                
            print("*************************************************************************")
            print("*                                                                       *")
            print("*  __This deck is now playable but not rigorous and it has %s cards.__  *"%(len(deck)))
            print("*                                                                       *")
            print("*************************************************************************")
        else:
            print("************************************************************************")
            print("*                                                                      *")
            print("*  __This deck is now playable but not rigorous and it has %s cards.__  *"%(len(deck)))
            print("*                                                                      *")
            print("************************************************************************")
    else:
        if len(deck) >= 10:
            print("*********************************************************************")
            print("*                                                                   *")
            print("*  __This deck is now playable and rigorous and it has %s cards.__  *"%(len(deck)))
            print("*                                                                   *")
            print("*********************************************************************")
        else:
            print("********************************************************************")
            print("*                                                                  *")
            print("*  __This deck is now playable and rigorous and it has %s cards.__   *"%(len(deck)))
            print("*                                                                  *")
            print("********************************************************************")
        
    
    wait_for_player()
    clear_board()
    deck = shuffle_deck(deck)
    wait_for_player()
    clear_board()

    if len(deck) == 0:
        print("The resulting board is empty.")
        print("Playing Concentration game with an empty board is impossible.")
        print("Good bye")
    else:        
        play_game(deck)