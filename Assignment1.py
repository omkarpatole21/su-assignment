#Q1. What is a variable in Python? Explain with two examples.
#variable is use to store data or value
#for example: name="omkar", a=10
#In this examples omkar value store in variable 'name' and 10 value store in variable 'a'.


#Q2. Write a Python program to take two numbers as input and display their sum, difference, product, and quotient.

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# sum=a+b
# diff=a-b
# product=a*b
# quot=a/b
# print("sum is",sum)
# print("difference is",diff)
# print("product is",product)
# print("quotient is",quot)


#Q3. Write a Python program to swap two numbers (a) using a third variable, and (b) without using a third variable.

# a=10
# b=30
# print("before swap",a,b)
# temp=a
# a=b
# b=temp
# print("after swap",a,b)

a=10
b=30
a,b=b,a
print(a,b)


#Q4. Take the length and width of a rectangle as input and calculate its area and perimeter using Python.

# l=int(input("enter length:"))
# w=int(input("enter width:"))
# area=l*w
# p=2*(l+w)
# print("Area of rectangle",area)
# print("perimeter of rectangle",p)


#Q5. Suppose: a = 12 and b = 5
# Write Python statements to display the result of:
# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Modulus
# Exponentiation

# a=12
# b=5

# add=a+b
# sub=a-b
# mul=a*b
# div=a/b
# fdiv=a//b
# mod=a%b
# exp=a**b
# print("Addition:",add)
# print("Subtraction",sub)
# print("Multiplication",mul)
# print("Division",div)
# print("Floor Division",fdiv)
# print("Modulus",mod)
# print("Exponentiation",exp)


#Q6. Write a Python program to ask the user for their name and age, and then print the message:
#Hello <name>, you are <age> years old.

# name=str(input("enter your name:"))
# age=int(input("enter your age:"))

# print(f"Hello {name}, you are {age} years old.")


#Q7. Write a Python program to take a number as input and check whether it is even or odd using the modulus operator.

# a=int(input("enter a number:"))

# if a%2==0:
#     print("even")
# else:
#     print("odd")


#Q8. Write a Python program to take the marks of 5 subjects from the user, calculate the total marks and percentage, and display the result.

# s1=int(input("enter marks 1:"))
# s2=int(input("enter marks 2:"))
# s3=int(input("enter marks 3:"))
# s4=int(input("enter marks 4:"))
# s5=int(input("enter marks 5:"))

# total = s1+s2+s3+s4+s5
# per=total/5.0
# print("Total:",total)
# print("percentage:",per)


#Q9.x = 7 and y = 3
# Predict the output of the following before running the code, and then verify by executing in Python:
# x**y -> 343
# x//y -> 2
# x % y(x + y)*(x - y) -> 40

# x=7
# y=3
# print(x**y)
# print(x//y)
# print(x%y*(x+y)*(x-y))


#Q10. write a Python program that accepts three numbers from the user and prints their average

# a=int(input("enter a value:"))
# b=int(input("enter a value:"))
# c=int(input("enter a value:"))

# avg=(a+b+c)/3.0
# print("average",avg)