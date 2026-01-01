#Q1. Declare variables of type int, float, string, and bool in Python. Print their values and types using the type() function.

# a=10
# b=12.5
# c="om"
# d=True

# print(a)
# print(b)
# print(c)
# print(d)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


#Q2. Write a Python program that takes two integers from the user and prints:
# The sum of the numbers
# The difference between the numbers
# The product of the numbers

# a=int(input("enter a number:"))
# b=int(input("enter a number:"))

# c=a+b
# d=a-b
# e=a*b
# print("sum:",c)
# print("difference:",d)
# print("product:",e)


#Q3. Write a Python program to calculate the simple interest. Formula:
# (Take P, R, T as float input from the user).

# p = float(input("Enter the principal:"))
# r = float(input("Enter the annual interest rate:"))
# t = float(input("Enter the time in year:"))

# s=p*r*t/100
# print("Simple Interest:",s)


#Q4. Write a Python program that asks the user for their first name and last name and 
#    then prints the full name in reverse order (last name first, then first name).

# f_name=str(input("enter first name:"))
# l_name=str(input("enter last name:"))

# print(l_name,f_name)


#Q5. Suppose:
# a = 15
# b = 4.5
# c = "Python"
# d = True
# Find and print the data type of each variable.

# a = 15
# b = 4.5
# c = "Python"
# d = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


#Q6. Write a Python program that asks the user for a sentence (string) and prints:
# The sentence in lowercase
# The number of words in the sentence

# p=str(input("enter a sentence:"))
# print(p)

# print(p.lower())
# print(len(p))


#Q7. Write a Python program to check whether a given integer is odd or even. 
# Print the result as a boolean value (True for even, False for odd).

# a = int(input("enter a number:"))

# if a%2==0:
#     print(True)
# else:
#     print(False)


#Q8. Write a Python program that takes two float numbers as input and prints:
# Their sum as an integer (use type conversion)
# Their product as a float

# a =float(input("enter a number:"))
# b =float(input("enter a number:"))

# sum = a+b
# sum=int(sum)
# print("sum:",sum)

# prod=a*b
# print("product:",prod)


#Q9. Write a Python program to evaluate the following boolean expressions and display the results:
# 10 > 5 and 7 < 3
# 4*2 == 8 or 6/2 == 4
# not (15 < 20)

# print(10 > 5 and 7 < 3)
# print(4*2 == 8 or 6/2 == 4)
# print(not (15 < 20))


#Q10. Write a Python program that takes a floating-point number as input and displays its square and cube.

# a=10.5

# print("square:",a**2)
# print("cube:",a**3)