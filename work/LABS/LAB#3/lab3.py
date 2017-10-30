def pay(wage, total_hours):
    pay = 0
    if total_hours > 60:
        pay = pay + wage * 2 * (total_hours - 60)
        total_hours = total_hours - (total_hours-60)

    if total_hours > 40:
        pay = pay + wage * 1.5 * (total_hours - 40)
        total_hours = total_hours - (total_hours - 40)
    
    pay = pay + total_hours * wage

    return pay

def rps(player_one, player_two):
    possible_values = {'SS' : 0, 'RR' : 0, 'PP' : 0, 'SR' : 1, 'PS' : 1, 'RP' : 1, 'RS' : -1, 'SP' : -1, 'PR' : -1}
    return possible_values[player_one+player_two]

def is_divisible(n = None, m =None):
    if n == None or m == None:
        n = int(input('Enter 1st integer: '))
        m = int(input('Enter 2nd integer: '))

    if n % m == 0:
        print(str(n) + " is divisible by " + str(m))
        return True
    
    print(str(n) + " is not divisible by " + str(m))
    return False

def is_divisible23n8():
    n = int(input('Enter an integer: '))
    if is_divisible(n, 2) or is_divisible(n, 3) and not is_divisible(n, 8):
        print("%s is divisible by 2 or 3 but not 8"%(n))
    else:
        print("It is not true that %s is divisible by 2 or 3 but not 8"%(n))


# print(rps('R', 'P'))