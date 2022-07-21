# Question 1
#1) False 
#2) <class 'list'>
#   <class 'list'>
# Question 2 (1)
# def getNumbersFromFunc():
#        x=y=z=10
#        print (x)
#        print (y)
#        print (z)
    
# getNumbersFromFunc()
#(2)
# def sumof():
#     x=input("Enter first number\n")
#     y=input("Enter second number\n")
#     print(int(x)+int(y))
# sumof()
#Question 3 (1)
# def palindrome(x):
#     temp = x
#     rev = 0
#     while x > 0:
#         lastdigit = x % 10
#         rev = (rev * 10) + lastdigit
#         x = x // 10
#     if temp == rev:
#         print("palindrome")
#     else:
#         print("not palindrome")
# palindrome(121)
# palindrome(125)
#(2)
# def merge(listx, listy):
#     listr=[]
#     for i in listx:
        
#      if i % 2 != 0:
#       listr.append(i)
#     for j in listy:
        
#      if j % 2 ==0:
#       listr.append(j)
#       return listr

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 61, 75, 93]
# print(merge(list1, list2))
#(3)
# def exponent(base,exp):
#     print("The result is:",int(base**exp))
# exponent(2,2) 
#(4)
# num=int(input("Enter a number\n"))
# for i in range(1,11,1):
#     mult=num*i
#     print(mult)
#(5)
# list = [1, 2, 3, 4, 5]
# lsize=len(list) - 1
# for i in range(lsize,-1,-1):
#     print(list[i])
# (6)  
# start = int(input("Enter first number of range\n"))
# end= int(input("Enter the number of at the end of the range\n")) 
# for i in range(start,end + 1):
#     if i >1:
#         for j in range(2,i):
#             if(i % j == 0):
#                 break
#         else:
#             print(i)
# (7)  
# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)
#(8)
# def checkt(tuple):
#     return all(i == tuple[0] for i in tuple)
# tuple = (1, 1, 1, 1)
# print(checkt(tuple))	  