from cmath import pi
import string
import random
# Question 1

#1 list and tuples are both a type of data structure/container type that are built in and defined in python.
# lists tend to be more mutable than tuples meaning lists can be changed while the other not, 
# so some operations work on lists but not tuples 

#2 Break is used to end a loop or a conditional statement without the compiler reading the condition.
# Continue is used to force the loop to do the next iteration of the loop skipping the code after the continue statement.
# Pass is used to skip a part of code without error for example writing an empty loop with no code to execute in it.
 
#3 Self is used to represent an object of a class, meaning one class can have 2 objects of the same type with different values of their attributes.

#4 Docstrings are used after defining a class, function or method to document the code written docstrings can be printed using "print(FunctionName.__doc__)"

# 5 Multiple inheritance is when a class inherits all attributes/features from more than one class

# Question 2 T or F
#1 F, takess space in compiler memory
#2 F, divided classes
#3 T
#4 F, a constructor does not have a return type not even void
#5 T

# Question 3
# 1 vowel count
# def count_vowels():
#     str=input("type a word or sentence\n")
#     count=0
#     for char in str:
#         if char in "AEIOUaeiou":
#             count=count +1
#     return print(count)         
# count_vowels()   

# 2 Sum of natural numbers
# def sum_numbers(x):
#        if x<=1:
#         return x
#        else:
#         return x + sum_numbers(x-1) 
# print(sum_numbers(16))

# 3 Fibonacci series
# def fib(x):
#     y = 0
#     z = 1
#     if x == 1:
#         print(y)
#     else:
#         print(y)
#         print(z)
#         for i in range(2,x):
#             f = y + z
#             y = z
#             z = f
#             print(f)
# fib(10)

# 4 Check in dictionary
# sample_dict ={'a':100,'b':200,'c':300}
# if 200 in sample_dict.values():
#     print("200 present in a dict")
# else:
#     print("200 not present in a dict")

# 5 circle and cylinder class
# class circle:
#     __radius = 1.0
#     __color="red"
#     def Circle():
#         pass
#     def Circle(self,radius):
#         self.__radius=radius
#     def Circle(self,radius,color):
#         self.__radius=radius
#         self.__color=color
#     def getRadius(self):
#         return self.__radius
#     def setRadius(self,radius):
#         self.__radius=radius 
#     def getColor(self):
#         return self.__color
#     def setColor(self,color):
#            self.__color=color            
#     def getArea(self):
#         return 2 * pi * self.__radius
#     def ToString(self):
#         return str(self.__radius),str(self.__color)  

# class cylinder(circle):
#     __height=1.0
#     def Cylinder():
#         pass
#     def Cylinder(self,radius):
#         self.radius=radius
#     def Cylinder(self,radius,height):
#         self.__radius=radius
#         self.__height=height
#     def Cylinder(self,radius,height,color):
#         self.__radius=radius
#         self.__height=height
#         self.__color=color
#     def getHeight(self):
#         return self.__height 
#     def setHeight(self,height):
#         self.__height=height
#     def getVolume(self):
#               return pi * (self.__radius*self.__radius) * self.__height        

# Question 4
# 1 Generate random password
# u = list(string.ascii_uppercase) #40%
# l = list(string.ascii_lowercase) #30%
# n = list(string.digits)#30%
# def genPassword():
#     passwordlen = int(9)
#     password = []
#     random.shuffle(u)
#     random.shuffle(l)
#     random.shuffle(n)
#     for i in range(round(passwordlen * .4)):
#         password.append(u[i])
#     for i in range(round(passwordlen * .3)):
#         password.append(l[i])
#     for i in range(round(passwordlen * .3)):
#         password.append(n[i]) 
#     password = "".join(password[0:])
#     print(f"Password is:\n {password}")

# genPassword()

# Question 5
# 1 Default constructor vs parameterized constructor 

# Default constructor: automatically generated by compiler if there is no programmer created contsructors,
# has no parameters, automatically called if there is no programmers constructor.

# Parameterized constructor: created by programmers with one or more parameters to initialize variables.   

# 2 Class vs object

# A class is used to create and declare objects, take no space in memory, declared only one time
# An object is an instance of a class, allocated in memory when created, can be declared as much as wanted.