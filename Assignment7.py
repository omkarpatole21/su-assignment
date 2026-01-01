# Q1. Write a lambda function to calculate the square of a given number. Call it with different inputs.

# b=lambda a: a*a
# print(b(3))
# print(b(2))


# Q2. Write a lambda function to check whether a given number is even or odd.

# b=lambda a:"even" if a%2==0 else "odd"
# print(b(3))
# print(b(8))


# Q3. Write a lambda function to find the maximum of two numbers.

# b=lambda a,b:a if a>b else b
# print(b(3,6))
# print(b(10,5))


# Q4. Write a lambda function to sort a list of tuples based on the second element.
# Example: [(1, 5), (2, 1), (3, 4)] -> [(2, 1), (3, 4), (1, 5)].

# a=[(1, 5), (2, 1), (3, 4)]
# b=sorted(a,key=lambda a:a[1])
# print(b)


# Q5. Write a program that uses map() with a lambda function to calculate the square of each number in the 
# list [1, 2, 3, 4, 5].

# l=[1,2,3,4,5]
# b=list(map(lambda a:a*a,l))
# print(b)


# Q6. Write a program that uses map() with a lambda function to convert a list of names into uppercase. 
# Example: ["shraddha", "rahul", "anjali"] -> ["SHRADDHA", "RAHUL", "ANJALI"].

# name=["shraddha", "rahul", "anjali"]
# b=list(map(lambda a:a.upper(),name))
# print(b)


# Q7. Write a program that uses filter() with a lambda function to extract only the even numbers from the 
# list [10, 21, 32, 43, 54, 65].

# l=[10, 21, 32, 43, 54, 65]
# b=list(filter(lambda a:a%2==0,l))
# print(b)


# Q8. Write a program that uses filter() with a lambda function to select the words that start with the letter "A" 
# from the list [ "Apple", "Banana", "Apricot", "Mango", "Avocado"].

# l=[ "Apple", "Banana", "Apricot", "Mango", "Avocado"]
# b=list(filter(lambda a:a=="A%",l))
# print(b)


# Q9. Write a program that uses reduce() with a lambda function to calculate the sum of all numbers in the 
# list [5, 10, 15, 20, 25].
from functools import reduce

# l=[5, 10, 15, 20, 25]
# b=reduce(lambda a,b: a+b,l)
# print(b)


# Q10. Write a program that uses reduce() with a lambda function to find the maximum number in the 
# list [12, 45, 67, 23, 89, 34].

# l=[12, 45, 67, 23, 89, 34]
# b=reduce(lambda a,b:a if a>b else b,l)
# print(b)


# Q11. Write a program that takes a list of numbers, uses map() with a lambda to calculate their squares, 
# filter() to keep only even squares, and finally reduce() to calculate the sum of those even squares.

a=[1,2,3,4,5,6,7,8,9,10]
b=list(map(lambda a:a*a,a))
c=list(filter(lambda a:a%2==0,b))
d=reduce(lambda a,b:a+b,c)
print("Square:",b)
print("only even squares:",c)
print("sum of even squares:",d)


# Q12. Write a program that sorts a list of strings using a lambda function based on their length.
# Example: ["apple", "banana", "kiwi", "grapes"] → ["kiwi", "apple", "grapes", "banana"].

# l=["apple", "banana", "kiwi", "grapes"]
# b=list(sorted(l,key=lambda a:len(a)))
# print(b)


# Q13. Write a program that uses a lambda function with filter() to extract palindromes from a list of strings.
# Example: ["madam", "python", "level", "hello"] → ["madam", "level"].

l=["madam", "python", "level", "hello"]
b=list(filter(lambda a:a[::-1]==a,l))
print(b)

# for i in l:
#     # print(i)
#     if i[::-1]==i:
#         print(i)
    