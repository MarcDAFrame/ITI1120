
# example 1
def sum_odd(n):
     ''' (num)->num
     Returns the sum of positive odd numbers smaller than n'''
     odd_sum = 0
     for num in range(n):
          if num % 2 == 1:
               odd_sum = odd_sum + num
     return odd_sum  

result=sum_odd(12)      
print(result)

# Exercise 1

def ah(l,x,y):
  return_list = []
  for i in l:
    if i >= x and i <= y:
      return_list.append(i)
  return return_list

# example 2
def product_odd(n):
     ''' (num)->num
     Returns the product of all positive odd numbers smaller than n'''
     prod = 1 
     for num in range(n):
          if num % 2 == 1:
               prod = prod * num
     return prod  

result=product_odd(12)      
print(result)

# example 3
def sum_list_v1(a):
   ''' (list)->num
     Returns the sum of the odd elements in a given list a'''
   list_sum = 0
   for item in a:
      if item % 2 == 1:
         list_sum = list_sum + item
   return list_sum

lst=[10,21,3]
result=sum_list_v1(lst)
print(result)


#example 4
def sum_list_v2(a):
    ''' (list)->num
     Returns the sum of the odd elements in a given list a'''
    list_sum = 0
    for i in range(len(a)):
       if a[i] % 2 == 1:
          list_sum = list_sum + a[i]
    return list_sum

lst=[10,21,3]
result=sum_list_v2(lst)
print(result)
