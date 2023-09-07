friends = ["Kevin", "Karen", "Jim"]

print(friends)  # ['Kevin', 'Karen', 'Jim']
print(friends[0]) # Kevin

#taking the elements after the index:1 -  including 1
print(friends[1:]) #['Karen', 'Jim']

#replacing value
friends[1] = "New Karen"
print(friends) #['Kevin', 'New Karen', 'Jim']


my_friends = ["Kevin", "Karen", "Jim", "Oscar", "Tom", "Ben"]

#taking the elements have index 2, 3 - including 2 but not including 4
print(my_friends[2:4]) #['Jim', 'Oscar']

# List functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
names =  ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
print(names) #['Kevin', 'Karen', 'Jim', 'Oscar', 'Tom']

names.extend(lucky_numbers)
print(names) #['Kevin', 'Karen', 'Jim', 'Oscar', 'Tom', 4, 8, 15, 16, 23, 42]

names =  ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
names.append("Havva")
print(names) #['Kevin', 'Karen', 'Jim', 'Oscar', 'Tom', 'Havva']

names =  ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
names.insert(1, "Havva")
print(names) #['Kevin', 'Havva', 'Karen', 'Jim', 'Oscar', 'Tom']


names =  ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
names.remove("Jim")
print(names) #['Kevin', 'Karen', 'Oscar', 'Tom']

names =  ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
names.pop() #removes the last one 
print(names) # ['Kevin', 'Karen', 'Jim', 'Oscar']


names =  ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
names.clear()
print(names) # []

names =  ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Tom"]
print(names.count('Jim')) #3 

lucky_numbers.sort()
lucky_numbers.reverse()

friends2 = friends.copy()