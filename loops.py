# what is a loop?
# a loop is used to repeat a block of code multiple tyms until a condition is met.

# types of loops in py

# 1. for loop
# used when weknow how many tyms we want to repeat a block of code.

# syntax
# for variable in sequence:
    #code

# range() func used to generate sequence of nums

# range comes with 3 parameters
# 1. start (inclusive)
# 2. stop (exclusive)
# 3. step (optional, deafault is 1)

# range(start, stop, step)

# example:
# for i in range(1,6):
#     print(i)

# key points:
# range(start,stop) generates numbers
# loop runs fixed number of tyms

# 2. while loop
# used when we repeat until a condition becomes false.

# syntax:
# while condition:
    #code

# example:
# i=1
# while i<=5:
#     print(i)
#     i+=1

# loop control statements:

# 1. break: stops loop immidiately
# ex 
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# 2. continue: skips current iteration
# ex
# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i)

# 3. pass: does nothing, used as a placeholder
# ex
# for i in range(5):
#         pass

# TASK:
# PRINT 1 TO 10 USING FOR LOOP

# for i in range(1, 11):
#     print(i)

# TASK:
# EVEN NUMBERS FROM 1 TO 20

# for i in range(1, 21):
#     if i%2==0:
#         print(i)

# for i in range(2, 21, 2):
#     print(i)

# for i in range(21, 1, -1):           -ve value for decreasing order
#     print(i)

# TASK:
# ODD NUMBERS FROM 1 TO 15

# for i in range(1, 16):
#     if i%2!=0:
#         print(i)

# TASK:
# print each character of the string

# name="Python"
# for char in name:
#     print(char)

# TASK:
# print all items in the list

# course=["Python", "Java", "C++", "JavaScript"]
# for item in course:
#     print(item)

# TASK:
# sum of numvers from 1 to 10

# total=0
# for i in range(1, 11):
#     total+=i
# print("Sum of numbers 1 to 10 :", total)

# TASK:
# print multiplication table of 5

# num = 5
# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")

# TASK:
# COUNT HOW MANY VOWELS IN A STRING

# string = "Hello World"
# vowels = "aeiouAEIOU"
# count = 0
# for char in string:
#     if char in vowels:
#         count += 1
# print(f"Number of vowels in '{string}' is: {count}")

# TASK:
# print nums in reverse order from 1 to 10

# for i in range(10, 0, -1):
#     print(i)

# TASK:
# square of nums from 1 to 5

# for i in range(1, 6):
#     print(f"Square of {i} is {i**2}")


