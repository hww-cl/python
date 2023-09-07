num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = num1 + num2
print(result)

# Enter a number: 5
# Enter another number: 3.8
# 53.8
# this is wrong , python makes it string , we should return it to number


result = int(num1) + int(num2)
print(result)

# Enter a number: 5
# Enter another number: 3.4
# ValueError: invalid literal for int() with base 10: '3.4'


result = float(num1) + float(num2)
print(result)

# Enter a number: 5
# Enter another number: 3.4
# 8.4