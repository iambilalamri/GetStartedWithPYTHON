# CONTROL FLOW
print("#######################################")

print(10 == "10")  # False
print(10 != "10")  # True
print("bag" > "apple")  # True
print("bag" == "BAG")  # False
print(ord('b'))  # 98
print(ord('a'))  # 97
print(ord('B'))  # 66

# CONDITIONNAL STATEMENT
print("########################################")

temperature = 27
if temperature > 30:
    print("It's warm")
    print("Drink Water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's Cold")
print("Done")

# TERNARY OPERATOR
print("##########################################")
age = 22
message2 = "Eligible" if age >= 18 else "Not Eligible"
print(message2)

# LOGICAL OPERATOR
print("##########################################")
high_income = True
good_credit = True
student = True

# and & or & not
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# ex: age should be between 18 and 65
age = 22
# if age < 65 and age >= 18:
if 18 <= age < 65:
    print("Eligible")

# EXERCICE
print("###########################################")
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

# LOOP
print("###########################################")
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# precise the range

for number in range(1, 4):
    print("Attempt", number, (number) * ".")

# increment by 2 in loop

for number in range(1, 10, 2):
    print("Attempt", number, (number) * ".")

# if else

successfull = False
for number in range(3):
    print("Attempt")
    if successfull:
        print("Successfull")
        break
else:
    print("Attempt 3 times and failed")

# Nested loop

for x in range(5):  # outer loop
    for y in range(3):  # inner loop
        print(f"({x}, {y})")

print(type(5))  # <class 'int'>
print(type(range(5)))  # <class 'range'>

# range and string and list are iterable
# ex: for i in "Python":

# While Loop1

number = 100
while number > 0:
    print(number)
    number //= 2

# While Loop2
# command1 = ""
# while command1.lower() != "quit":
#     command1 = input(">")
#     print("ECHO", command1)

# While Loop3
while True:
    command2 = input(">")
    print("ECHO", command2)
    if command2.lower() == "quit":
        break

# Exercice
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
