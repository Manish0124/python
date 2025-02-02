# def square(num):
#   return  num**2


# i = square(3)
# # print(i)
# print(square(4))


# def multiply(a1,a2):
#     return a1*a2

# print(multiply(4,5))
# print(multiply(4,'e'))

# function to calculate the area and  circumfrence by its radius
# import math

# def area_circumfrence(r):
#     a = 3.14*(r**2)
#     c = 2*3.14*r
#     return a,c


# print(area_circumfrence(2))


# to greet a user 

def greet(name = "ronny"):
    print("hello"+" "+name)


# greet()

# lambda function

cube = lambda x : x**3

# print(cube(2))

def sum_all(*args):
   return sum(args)


# print(sum_all(1,23,3,4))
# print(sum_all(1,23))
# print(sum_all(1,23,9,8))


# def kw_args(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# kw_args(hero="shaktiman", power="spin")
# kw_args(hero="shaktiman", power="spin", enemy="kilwish")


# yield

# def even_generatore(limit):
#     for i in range(2,limit+1,2):
#        yield i 



# for num in even_generatore(10):
#     print(num)


# factorial of a number

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)    

print(factorial(5))