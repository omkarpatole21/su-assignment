# 1. Check Number Type
# Write a Python program that accepts an integer from the user and 
# checks whether the number is positive, negative, or zero using if, elif, and else.

# a=int(input("enter a number:"))

# if a>0:
#     print("Positive number")
# elif a<0:
#     print("Negative number")
# else:
#     print("zero")


# 2. Even or Odd Number
# Write a program to accept an integer from the user and determine whether it is an even number or an odd number.

# num = int(input("enter a number"))

# if num%2==0:
#     print("Even")
# else:
#     print("Odd")


# 3. Largest of Three Numbers
# Write a Python program that accepts three integers from the user and prints which one is the largest number. 
# If all numbers are equal, display "All numbers are equal".

# a=int(input("enter a number1:"))
# b=int(input("enter a number2:"))
# c=int(input("enter a number3:"))

# if a>b and a>c:
#     print("A is largest")
# elif b>a and b>c:
#     print("B is largest")
# elif c>a and c>b:
#     print("C is largest")
# else:
#     print("All numbers are equal")


# 4. Student Grading System
# Write a program that accepts a student's marks (between 0 and 100) and prints the grade according to the following conditions:
# Marks ≥ 90 → Grade A
# Marks between 75 and 89 → Grade B
# Marks between 50 and 74 → Grade C
# Marks below 50 → Fail

# marks = int(input("enter marks (between 0 and 100):"))

# if marks >= 90:
#     print("Grade A")
# elif marks>=75 and marks<=89:
#     print("Grade B")
# elif marks>=50 and marks<=74:
#     print("Grade C")
# else:
#     print("Fail")


# 5. Leap Year Check
# Write a Python program to check whether a given year entered by the user is a leap year or not.

# year = int(input("Enter a year:"))

# if year%4==0:
#     print("Leap year")
# else:
#     print("not leap year")


# 6. Voting Eligibility
# Write a program that accepts the age of a person and checks whether the person is eligible to vote (18 years and above). 
# If the age is less than 18, print how many years are left until the person becomes eligible.

# age=int(input("Enter the age:"))

# if age>=18:
#     print("Eligible to vote")
# else:
#     a=18-age
#     print(f"{a} years are left to eligible for vote")


# 7. Traffic Light Simulation
# Write a program that simulates a traffic light system. Accept a color name ("Red", "Yellow", or "Green") 
# from the user and display the appropriate message:
# "Red" → "Stop"
# "Yellow" → "Ready"
# "Green" → "Go"
# If the input is not one of these three colors, display "Invalid Input".

# color = str(input("Enter a color ('Red', 'Yellow', or 'Green')"))

# if color=="Red" or color=="red":
#     print("Stop")
# elif color=="Yellow" or color=="yellow":
#     print("Ready")
# elif color=="Green" or color=="green":
#     print("Go")
# else:
#     print("Invalid Input")


# 8. Shopping Discount Calculator
# A store gives discounts based on the purchase amount:
# Above ₹5000 20% discount
# Between 2000 and ₹5000 10% discount
# 0 Below ₹2000 → No discount
# Write a program to accept the purchase amount and calculate the discount and the final amount to be paid.

# amount=float(input("Enter a amount:"))

# if amount > 5000:
#     dis=amount*20/100
#     print(f"You get 20% discount \nfinal amount to be paid is {amount-dis}")
# elif amount>=2000 and amount<=5000:
#     dis=amount*10/100
#     print(f"You get 10% discount \nfinal amount to be paid is {amount-dis}")
# else:
#     print("No discount \nYour paid amount is",amount)


# 9. Password Authentication
# Write a Python program that asks the user to enter a password.
# If the entered password matches "admin123", print "Access Granted".
# Otherwise, print "Access Denied".

# password = str(input("Enter a password:"))

# if password=="admin123":
#     print("Access Granted")
# else:
#     print("Access Denied")


# 10. Day of the Week Finder
# Write a program that accepts a number between 1 and 7 from the user 
# and prints the corresponding day of the week (1→ Monday, 2 Tuesday,... 7 Sunday).
# If the input is not between 1 and 7, display "Invalid Input".

# a=int(input("Enter a number between 1 and 7: "))

# if a==1:
#     print("Monday")
# elif a==2:
#     print("Tuseday")
# elif a==3:
#     print("Wednesday")
# elif a==4:
#     print("Thursday")
# elif a==5:
#     print("Friday")
# elif a==6:
#     print("Saturday")
# elif a==7:
#     print("Sunday")
# else:
#     print("Invalid Input")