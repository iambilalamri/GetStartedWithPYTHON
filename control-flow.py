# CONTROL FLOW
#######################################

print(10 == "10")  # False
print(10 != "10")  # True
print("bag" > "apple")  # True
print("bag" == "BAG")  # False
print(ord('b'))  # 98
print(ord('a'))  # 97
print(ord('B'))  # 66

# CONDITIONNAL STATEMENT
########################################

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
##########################################
age = 22
message2 = "Eligible" if age >= 18 else "Not Eligible"
print(message2)

# LOGICAL OPERATOR
##########################################
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
###########################################
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
