# Variables 
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + "years old")
print("He really liked the name " + character_name )
print("but didn't like being " + character_age)


# String methods
phrase = "My Pyhton Journey"
print(phrase)  # My Pyhton Journey
print(phrase.lower()) #my pyhton journey
print(phrase.upper()) #MY PYHTON JOURNEY
print(phrase.isupper()) #False
print(phrase.upper().isupper()) #True
print(len(phrase)) #17 length of the string
print(phrase[0]) #M
print(phrase.index("P")) #4
print(phrase.replace("My", "Your")) #Your Pyhton Journey

#Numbers 
print(2)
print(2+4) #
print(-2.0647)

print(3 * 4 + 5) #17 
print(3 * (4 + 5)) #27

print(10 % 3) #1

my_num = 5
print(my_num) #5
# print(my_num + "my favorite number") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(my_num) + " is my favorite number") #5 is my favorite number


my_num = -5
print(my_num) # -5
print(abs(my_num)) # 5
print(pow(my_num, 3)) # -125


print(max(4, 6)) #6
print(min(4, 6)) #4

print(round(3.7)) #4
print(round(3.2)) #3


from math import *
print(ceil(3.1)) #4
print(floor(3.2)) #3
print(sqrt(36)) #6


