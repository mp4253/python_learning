# fruits = ["apple", "banana", "kiwi", "pineapple"]
# print(fruits)
# print(type(fruits))

# --------------------------------------------------------------

# range()

# start, stop, skip  -------->>> range function

# for i in range(1,22,2):    
#     print(i)

# for i in range(10,1,-1):
#     print(i)

# Print numbers from 5 to 15

# for num in range(5,16):
#     print(num)


# Print all odd numbers between 1 to 20

# for num in range(1,20):
#     if(num%2 != 0):
#         print("this are the all odd numbers.", num)


# Print the square of numbers from 1 to 10

# for num in range(1,11):
#     print(f"Square of {num} is:",num*num)


# Find the sum of even numbers from 1 to 100

total = 0

# for num in range(1,101):
#     if(num%2 == 0):
#         total = total + num
    
# print(f"The sum of all even numbers is:",total)


# Print this pattern:
# *
# **
# ***
# **** 

# for num in range(1,5):
#     print("*" * num)
    
# Print this pattern:
# ****
# ***
# **
# * 

for i in range(5,0,-1):
    print("*" * i)
    

