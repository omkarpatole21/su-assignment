# Answer the following questions based on list operations:
# 1. Create a list of 5 fruits.
# 2. Print the first and last element of the list.
# 3. Display elements from index 2 to 4 using slicing.
# 4. Append "Mango" to the fruit list.
# 5. Insert "Banana" at index 1.
# 6. Remove "Apple" from the list.
# 7. Remove the last element using the pop() method.
# 8. Sort a list of numbers in ascending order.
# 9. Reverse the list of numbers.
# 10. Check whether "Orange" exists in the list or not.

# fruits = ["Apple","Orange","Grapes","Berry","Pear"]

# print("first element:",fruits[0])
# print("last element:",fruits[-1])

# print(fruits[2:5]) #display element from 2 to 4

# fruits.append("Mango") #append Mango in list
# print(fruits)

# fruits.insert(1,"Banana") #insert banana at index 1
# print(fruits)

# fruits.remove("Apple") #remove apple from list
# print(fruits)

# fruits.pop() #remove last element from list
# print(fruits)

# fruits.sort() 
# print(fruits)

# fruits.reverse()
# print(fruits)

# print("Orange" in fruits) 


# Answer the following questions based on tuple operations:
# 1. Create a tuple containing 6 colors.
# 2. Print the 3rd element of the tuple.
# 3. Display elements from index 1 to 4 using slicing.
# 4. Count how many times "Red" appears in the tuple.
# 5. Find the index of "Blue" in the tuple.
# 6. Find the length of the tuple.
# 7. Convert the tuple into a list, add "Black", and then convert it back into a tuple.

# color = ("Red","Orange","Black","Blue","Red","Green")

# print(color[3])

# print(color[1:5])

# print(color.count("Red"))

# print(color.index("Blue"))

# print(len(color))

# color = list(color)
# color.append("Black")
# color = tuple(color)
# print(color)


# Answer the following questions based on set operations:
# 1. Create a set of prime numbers less than 20.
# 2. Add the number 19 to the set.
# 3. Remove the number 7 from the set.
# 4. Find the union of sets {1,2,3} and {3,4,5}.
# 5. Find the intersection of sets {2,4,6,8} and {4, 8, 12, 16}.
# 6. Find the difference between sets {10,20,30} and{20,40,50}.
# 7. Find the symmetric difference between sets {1,2,3,4} and {3,4,5,6}.
# 8. Remove duplicates from the list [1,2,2,3, 4, 4, 5] using a set.

# s ={2,3,5,7,11,13,17}

# s.add(19) # add 19 in set
# print(s)

# s.remove(7)
# print(s)

# a={1,2,3}
# b={3,4,5}
# print("union:",a.union(b))

# a={2,4,6,8}
# b={4,8,12,16}
# print("Intersection:",a.intersection(b))

# a={10,20,30}
# b={20,40,50}
# print("Difference:",a.difference(b))

# a={1,2,3,4}
# b={3,4,5,6}
# print("symmetric difference:",a.symmetric_difference(b))

# l=[1,2,2,3,4,4,5]
# l=set(l)
# print(l)


# Answer the following questions based on dictionary operations:
# 1. Create a dictionary with student names as keys and their ages as values.
# 2. Print the age of a student "Rahul".
# 3. Add a new entry "Anjali": 20.
# 4. Update "Rahul"'s age to 22.
# 5. Delete the entry for "Sneha".
# 6. Print all keys from the dictionary.
# 7. Print all values from the dictionary.
# 8. Print all key-value pairs from the dictionary.
# 9. Find the number of items in the dictionary.
# 10. Count the frequency of each word in the string "apple banana apple orange banana apple".

d = {"Om":21,"sahil":30,"luv":32,"Rahul":40,"Sneha":19}

print("age of Rahul:",d["Rahul"]) 

d["Anjali"] = 20
print(d)

d["Rahul"] = 22
print(d)

del d["Sneha"]
print(d)

print(d.keys())

print(d.items())

print(len(d))


string="apple banana apple orange banana apple"

a=string.split()
print(a)
print("apple:",a.count("apple"))
print("banana:",a.count("banana"))
print("orange:",a.count("orange"))