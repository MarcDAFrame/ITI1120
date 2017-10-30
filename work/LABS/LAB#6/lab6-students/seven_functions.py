
# sum of positive odd integers smaller than n
# with for loop
def sum_odd_for(n):
   odd_sum = 0
   for num in range(n):
      if num % 2 == 1:
         odd_sum = odd_sum + num
   return odd_sum  

result=sum_odd_for(12)      
print(result)

# sum of positive odd integers smaller than n
# with while loop
def sum_odd_while(n):
   odd_sum = 0
   i=1    # need to initialize
   while i < n: 
      if i % 2 == 1:
          odd_sum = odd_sum + i
      i=i+1 
# need to increment
   return odd_sum

result=sum_odd_while(12)      
print(result)

# Sum of odd numbers in a given list a
# with for loop
def sum_list_for(a):
    ''' (list)->num
     Returns the sum of the odd elements in a given list a'''
    list_sum = 0
    for i in range(len(a)):
       if a[i] % 2 == 1:
          list_sum = list_sum + a[i]
    return list_sum

lst=[10,21,3]
result=sum_list_for(lst)
print(result)

# Sum of odd numbers in a given list a
# with while loop
def sum_list_while(a):
    ''' (list)->num
    Returns the sum of the odd elements in a given list a'''
    list_sum = 0
    i=0
#initialize
    while i < len(a):
       if a[i] % 2 == 1:
          list_sum = list_sum + a[i]
       i=i+1 
# increment 
    return list_sum

lst=[10,21,3]
result=sum_list_while(lst)
print(result)

# finding minimum with for loop over elements of the list a
def minimum_for_v1(a):
   ''' (list)->num
   Returns a minimum element in a list
   Precondition: length of list a is at least 1'''

   minimum = a[0]
   for element in a:
      if element < minimum:
         minimum = element
   return minimum

#finding minimum with for loop over indices of list a
def minimum_for_v2(a):
   ''' (list)->num
   Returns a minimum element in a list
   Precondition: length of list a is at least 1'''

   minimum = a[0]
   for i in range(len(a)):
      if a[i] < minimum:
         minimum = a[i]
   return minimum


### finding minimum with while loop
def minimum_while(a):
   ''' (list)->num
   Returns a minimum element in a list
   Precondition: length of list a is at least 1'''

   minimum = a[0]
   i=0
   while i < len(a):
      if a[i] < minimum:
         minimum = a[i]
      i=i+1
   return minimum
