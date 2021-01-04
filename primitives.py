### PRIMTIVE TYPES ###
# Pritive type in Python: strings, numbers(int, float, complex number), booleans
import math

##############################################
# CONVERSION
x = input("x: ")
print(type(x))  # <class 'str'>
y = int(x) + 1
print(f"x: {x}, y: {y}")
print(type(y))  # <class 'int'>

# int(x)
# float(x)
# bool(x)
# str(x)

# Equivalent of False = "", 0, None
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("False"))  # True
print(bool(None))  # False
print(bool(-1))  # True
print(bool(5))  # True

##############################################
# NUMBERS

# print(round(2.9))
# print(abs(-2.9))

# print(math.ceil(2.2))

# print(10+3)
# print(10*3)
# print(10-3)
# print(10/3)
# print(10//3)
# print(10 % 3)  # Modulo
# print(10**3)  # Power

# x = 10
# x = x+3
# x += 3

##############################################
# STRING METHOD

# string1 = "hello world of python"
# string2 = "     hello i am python junior"
# string1_capital = string1.upper()
# string1_lower = string1.lower()
# string1_title = string1.title()
# print(string1_title)
# string2_strip = string2.strip()  # remove a white space
# string2_lstrip = string2.lstrip()  # remove a left space
# string2_rstrip = string2.rstrip()  # remove a right space
# print(string2)
# print(string2_strip)
# print(string2.find("am"))  # 13
# print(string2.find("Am"))  # -1
# print(string1.replace("l", "x"))  # hexxo worxd of python
# print("am" in string2)  # True
# print("bro" not in string1)  # True

#############################################
# WAYS of SHOWING VARIABLES (CONCATENATION)

# first = "John"
# last = "Stewarts"
# full = first + " " + last
# example1 = f"{first} {last}"
# example2 = f"{len(first)} {len(last)} {4 + 3}"
# print(full)
# print(example1)
# print(example2)

##############################################
# Python is case sensitive language.
students_count = 1000
rating = 4.99
is_published = False
##############################################
# WAYS TO PRINT A STRING (ARRAY OF CHARS)
email_body = """
Hi, I am student forever

I want to learn from everybody
I hope your are doing good in this situation

Regards,
"""
# print(email_body)
# print(len(email_body))

course_name = "Python Programming"
# \n saut de ligne
# \ show special chars
course_label = "Python \"Language"
fruit = "Apple"
# print(course_label)
# print(students_count)
# print(len(course_name))
# print(course_name[0])   # P
# print(course_name[-1])  # g
# print(course_name[-2])  # n
# print(course_name[0:3])  # Pyt
# print(course_name[0:])  # Python Programming
# print(course_name[:3])  # Pyt
# print(course_name[:])  # Python Programming
# print(fruit[1:-1]) # ppl
