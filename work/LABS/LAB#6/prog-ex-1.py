def sum_odd_while_v2(n):
        '''(int)->int
        Returns the sum of all odd integers between 5 and n
        '''
        total = 0
        while n > 5:
                n = n - 1
                if n % 2 != 0:
                        total += n

        return total

print(sum_odd_while_v2(10))

