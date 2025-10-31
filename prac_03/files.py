# 1Write code that asks the user for their name, then opens a file called name.txt and writes that name to it
# Use open and close for this question

# 1.

user_name = input("Please input your name: ")

file = open("name.txt", "w")  # open file
file.write(user_name)  # write to file
file.close()  # close file

# 2.

file = open("name.txt", "r")  # open file
user_name = file.read()  # read file

print(f"Hi {user_name}!")  # print from file
file.close()  # colse file

# 3.

with open("numbers.txt", "r") as file:  # open file
    first_number = int(file.readline())  # read first line of file
    second_number = int(file.readline())  # read second line of file

total_number = first_number + second_number  # add the numbers

print(total_number)  # print the total

# 4.

total_number = 0  # initial total
with open("numbers.txt", "r") as file:  # open file
    for line in file:
        total_number += int(line.strip())  # add the numbers one by one

print(total_number)  # print total
