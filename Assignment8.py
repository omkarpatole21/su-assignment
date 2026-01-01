# Q1. Write a Python program to create a text file named student.txt and write the following 
# information into it:
# Name: Shraddha
# Age: 28
# Course: Python
# Then, read the file and display its contents.

# f = open("student.txt", "r")
# print(f.read())
# f.close()

# Q2. Write a program to accept a list of 5 fruits from the user, write them into a file fruits.txt,
#  and then read and print the file content line by line.

# fruits = []
# n=int(input("enter a number:"))
# for i in range(n):
#     fruit = input("Enter fruit name: ")
#     fruits.append(fruit + "\n")

# f = open("fruits.txt", "w")
# f.writelines(fruits)    
# f.close()

# f = open("fruits.txt", "r")
# print(f.read())
# f.close()


# Q3. Write a program to store 10 numbers into a file numbers.txt, 
# and then read and display only the even numbers from the file.

# numbers = []
# for i in range(10):
#     num = input("Enter a number: ")
#     numbers.append(num + "\n")

# f = open("numbers.txt", "a")
# f.writelines(numbers)
# f.close()

# f = open("numbers.txt", "r")
# for line in f:
#     num = int(line.strip())
#     if num % 2 == 0:
#         print(num)


# Q4. Create a file notes. txt with some initial content. Write a program to append the 
# following lines at the end of the file:

# This is an appended line.
# File handling in Python is easy.

# Then display the updated content.

# f = open("notes.txt", "a")
# f.write("\nThis is an appended line.\nFile handling in Python is easy.")
# f.close()

# f= open("notes.txt", "r")
# print(f.read()) 
# f.close()


# Q5. Write a program that allows the user to enter employee names one by one and appends them into 
# a file employees.txt. Stop when the user enters "stop". Finally, read and print all employee names.

# f = open("employees.txt", "a")
# while True:
#     name = input("Enter employee name: ")
#     if name == "stop":
#         break
#     f.write(name + "\n")
# f.close()

# f= open("employees.txt", "r")
# print(f.read())
# f.close()

# Q6. Write a program to count the number of words in a file story.txt.

# f = open("story.txt", "r")
# word=f.read().split()
# print("Number of words in the file:",len(word))
# f.close()
 

# Q7. Write a program to count the number of vowels in a file data.txt.

# vowels = "aeiouAEIOU"
# f = open("data.txt", "r")
# count = 0
# for i in f.read():
#     if i in vowels:
#         count += 1
# f.close()
# print("Number of vowels in the line:", count)

# Q8. Write a program that reads a file marks.txt containing student names and marks 
# (one per line, e.g., Rahul 85), and prints only the students who scored more than 50.

# f= open("marks.txt", "r")
# for line in f:
#     name, mark = line.split()
#     if int(mark) > 50:
#         print(name, mark)
# f.close()


# Q9. Write a program that reads a file sample.txt and writes its content into another file copy.txt.

# f= open("sample.txt", "r")
# f1= open("copy.txt", "w")
# f1.write(f.read())
# f.close()
# f1.close()

# Q10. Write a program to display the longest line from a file poem.txt.

# f = open("poem.txt", "r")
# longest_line = ""
# for line in f:
#     if len(line) > len(longest_line):
#         longest_line = line
# f.close()
# print("The longest line is:", longest_line)