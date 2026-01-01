#1. Print Natural Numbers
#Write a Python program using a for loop to print the first 10 natural numbers.

# for i in range(1, 11):
#     print(i)


# 2. Sum of First N Numbers
# Write a Python program that uses a while loop to calculate the sum of the first N natural numbers (N entered by the user).

# n=int(input("Enter a number:"))
# i=1
# sum=0
# while (i<=n):
#     sum=sum+i
#     i=i+1
# print(sum)


# 3. Multiplication Table
# Write a program that accepts a number from the user and prints its multiplication table up to 10 using a for loop.

# a=int(input("enter a number:"))
# for i in range(1,11):
#     i=a*i
#     print(i)

# 4. Factorial of a Number
# Write a Python program using a while loop to find the factorial of a given number.

# i=1
# n=int(input("Enter a number:"))
# fact=1
# while(i<=n):
#     fact=fact*i
#     i+=1
# print(f"Factorial of {n} is {fact}")

# 5. Reverse Counting
# Write a program using a for loop to print numbers from 100 down to 1.

# for i in range (100,0,-1):
#     print(i)

# 6. Even Numbers in a Range
# Write a Python program that prints all even numbers between 1 and 50 using a while loop.

# i=1
# while i<=50:
#     if i%2==0:
#         print(i)
#     i+=1


# 7. Sum of Digits
# Write a program using a while loop to calculate the sum of digits of a given number.

# num = int(input("Enter a number: "))
# sum = 0
# i=1

# while num > 0:
#     digit = num % 10      
#     sum += digit   
#     num = num // 10       

# print("Sum of digits:", sum)


# 8. Fibonacci Series
# Write a Python program using a for loop to display the first N terms of the Fibonacci series.

# n=int(input("Enter a number:"))
# a=0
# b=1
# print("Fibonacci series:")
# print(a)
# print(b)
# for i in range(1,n+1):
#     c=a+b
#     a=b
#     b=c
#     print(c)


# 9. Check Prime Number
# Write a program using a for loop to check whether a given number is prime or not.

# n = 2

# if n<=1:
#     print(f"{n} is not prime")
# else:
#     for i in range(1,n):
#         if n%i==0 and n!=2:
#             print(n,"is not prime")
#             break
#         else:
#             print(n,"is Prime number")


# 10. Number Guessing Game
# Write a Python program using a while loop for a number guessing game:
# The program sets a secret number (e.g., 25).
# The user keeps entering numbers until they guess correctly.
# Print "Too High" or "Too Low" as hints.
# End the loop when the user guesses the correct number.

# s_num=34

# while True:
#     guess_num=int(input("enter a number:"))

#     if guess_num>34:
#         print("Too High")
#     elif guess_num<34:
#         print("Too Low")
#     else:
#          print("You guessed it!")
#          break