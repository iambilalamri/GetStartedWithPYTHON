print("LISTS")
print("##########################################")
letters = ["a", "b", "c", "d"]
print(letters[-1])  # d
print(letters[0:3])  # [a, b, c]
print(letters[:3])  # [a, b, c]
print(letters[0:])  # [a, b, c, d]
print(letters[:])  # [a, b, c, d]


matrix = [[0, 1], [2, 3], [4, 5]]
zeros = [0] * 5  # array with 5 zeros
combined = letters + zeros  # combined string and number in same array
numbers = list(range(20))  # get a list of numbers of 0 to 19
chars = list("Hello World")  # get list of chars
print(numbers)
print(len(chars))
