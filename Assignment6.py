# Q1. Write a function named greet (name, message="Welcome") that prints a greeting message.
# Call the function by passing only the name argument.
# Call the function by passing both name and message arguments.

# def greet(name):
#     print("Welcome",name)
# greet("omkar")

# def greet(name, message):
#     print(message,name)
# greet("omkar",message="Welcome")


# Q2. Define a function power (base, exponent=2) that returns the result of raising the base to the exponent.
# Call the function with only the base argument.
# Call the function with both base and exponent arguments.

# def power(base):
#     c=base**2
#     print(c)
# power(3)

# def power(base,exp):
#     c=base**exp
#     print(c)
# power(2,2)


# Q3. Write a function student_info (name, age, city) that prints the details of a student.
# Call the function using positional arguments.
# Call the function using keyword arguments in a different order.

# def student_info(name,age,city):
#     print("Name:",name)
#     print("Age",age)
#     print("City",city)
# student_info("Sahil",22,"pune")
# student_info(name="om",city="mumbai",age=21)


# Q4. Define a function calculate_salary (basic, hra, da, bonus=0) that prints the total salary.
# Call the function using keyword arguments.
# Change the order of arguments while calling the function.

# def calculate_salary(basic, hra, da, bonus):
#     salary=basic+hra+da+bonus
#     print(salary)
# calculate_salary(2000,400,500,0)
# calculate_salary(hra=5000,da=500,bonus=20,basic=20000)


# Q5. Write a function sum_numbers (*numbers) that accepts any number of arguments and returns the sum of all numbers.

# def sum_numbers(*numbers):
#     total=sum(numbers)
#     print(total)
# sum_numbers(2,3,45)


# Q6. Define a function print_fruits (*fruits) that accepts multiple fruit names and prints them one by one.

# def print_fruits(*fruits):
#     print(fruits)
# print_fruits("mango","orange","banana")


# Q7. Write a function student_marks (**marks) that accepts subject names and marks as keyword arguments and 
# prints them in the format: Subject: Marks

# def student_marks(**marks):
#     for sub,mark in marks.items():
#         print(f"{sub} : {mark}")

# student_marks(Marathi=60,English=90,Maths=76)


# Q8. Create a function employee_details(**details) that accepts employee details 
# such as name, age, department, and salary. Print all details in a formatted way.

# def employee_details(**details):
#     for i,j in details.items():
#         print(f"{i}:{j}")

# employee_details(Name="sahil",age=32,department="Tester",salary=20000)


# Q9. Write a function book_details(title, author= "Unknown", **info) where:
# title is a required parameter
# author has a default argument
# **info can include other details such as price, publisher, and year
# Call the function by passing different combinations of arguments and print the details.

# def book_details(title, author= "Unknown", **info):
#     print("Title:",title)
#     print("Author",author)

#     for i,j in info.items():
#         print(f"{i}:{j}")

# book_details(title="Dune",price=2000,publisher="xyz",year=2002)


# Q10. Define a function order_food(item, quantity=1, *extras, **details) where
# item name of the food item
# quantity number of items (default = 1)
# *extras variable number of side dishes
# **details additional details such as table number, waiter name
# Write a program to call the function in at least two different ways and display the final order summary.

# def order_food(item, quantity=1, *extras, **details):
#     print(f"food item: {item}")
#     print(f"Quantity: {quantity}")

#     print(f"side dishes: {extras}")

#     for i,j in details.items():
#         print(f"{i}:{j}")

# order_food("Pizza",1,"Cheese","Sauce",table_number=20,waiter_name="sahil")