# Part 1

# Strings

# 1)

name = "Patryk "

print(name)

# 2)

last_name = "Okpara"

full_name = name + last_name

print(full_name)

# 3)

print(f"Hi, my name is {name}{last_name}")

# Integers

# 1)

num1 = 3
num2 = 66
result = num1* num2

print(result)

# 2)

print(f"The product of {num2} and {num1} is {result}")

# Lists

people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

# 1)

third = people[2]

print(third)

# 2)

back_third = people[-3]

print(back_third)

# 3)

people = people[2:6]

print(people)

# 4)

equal_or_no = people[0] == people[-1]

print(equal_or_no)

# Input

# 1)

# name = input("what is your name ?")

# print(name)

# 2)

# int1 = int(input("first number"))
# int2 = int(input("second number"))

# product = int1 * int2

# print(product)

# 3)

int_num = int(input("number"))

if int_num % 3 == 0 and int_num % 5 == 0:
    print ("FizzBuzz")
elif int_num % 3 == 0:
    print ("fizz")
elif int_num % 5 == 0:
    print ("buzz")

