# Parameter is the input that defined for function: like first_name
# Argument is the actual value given to parameter: like "Bilal"

# Two type of function:
# 1 - Perform a task

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Bilal", "AMRI")

# 2 - calculate and return value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("John")
print(message)

# Keyword Argument
# NOTE that all the optional paramters should come after the required ones


def increment(number, by=1):  # default value
    return number + by


print(increment(number=2))

# X-ARGUMENT


def mutiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(mutiply(2, 3, 4, 5))

# XX-ARGUMENT
# double stars will allow add keyword pair like (id=1)


def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])


# {'id': 1, 'name': 'John', 'age': 22} is object called dictionnary
save_user(id=1, name="John", age=22)
