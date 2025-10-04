#1Write code that asks the user for their name, then opens a file called name.txt and writes that name to it
#Use open and close for this question

#1.

user_name = input("Please input your name: ")

file = open("name.txt","w")
file.write(user_name)
file.close()


#2.

file = open("name.txt","r")
user_name = file.read()
file.close()

print(f"Hi {user_name}!")


#3.

file = open("numbers.txt","r")
first_number = int(file.readline())
second_number = int(file.readline())

total_number =  first_number + second_number

print(total_number)