# age = 50

# if age<20:
#     print("child")
# elif age<25:
#     print("seniour")
# elif age <50:
#     print("adult")
# else :
#     print("senior")


# What will be the output of the following code if the `age` is set to 11 and the `day` is "wednesday" and provide a discount of 2 if day is wednesday?

# age = 11

# day = "wednesday"

# price = 12 if age>=18 else 8

# if day == "wednesday":
#     price-=2



# print(price)
# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]

# postive_count = 0

# for num in numbers:
#     if num>0:   
#         postive_count+=1
# print(postive_count)



# n = int(input("enter the number from you want to check ?"))
# sum_even = 0
# for i in range(1,n+1):
#     if i%2==0:
#         sum_even+=1
# print("even number " ,sum_even)


# n = int(input("enter the number from table you want to know ?"))


# for i in range(1,n+1):
#         if i == 5:
#             continue
#         print(n,'X',i , n*i)


# for reverse the string 

# course = "Phython"

# reverse_string = ""

# # print(len(course))

# for char in course:
#     reverse_string = char + reverse_string 
# print(reverse_string)


# return the value when its find it first non -repeated character

# user_value = "teether"

# for char in user_value:
#     print(char)
#     if user_value.count(char) ==1:
#         print("non repeted character is ",char)
#         break


# calculate factorial value 

# number = 5
# factorial = 1

# while number >0 :
#     factorial *=number
#     number-=1
# print(factorial)    
  

#   taking input from the user until it value is beyond 1to10

# while True:
#     number = int(input("enter the no. b/w 1 to 10 : "))
#     if 1<=number<=10:
#         print("thanks")
#         break
#     else:
#         print("enter a valid input")


# check wheater the number is prime or not

# number = 8
# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             break

# print(is_prime)

# exit when you found the dublicate item 

# items = ["apple","mango","banana","apple", "pineapple"]

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("dublicate item", item)
#         break
#     unique_item.add(item)


# at every retries sleep down the timer 

import time 

print(time)

wait_time = 1
max_retries = 5;
attempt = 0

while attempt<max_retries:
    print("Attempts", attempt+1, "-wait time", wait_time,)
    time.sleep(wait_time)
    wait_time*=2;
    attempt+=1