def main():
    user_input_numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    user_name = input("please enter your username: ")     # ask user for username

    if user_name not in usernames:                  #check for valid username
        print("Access denied")
        return
    else:
        print("Access granted\n")

    for i in range(5):                           #set range
        numbers = int(input("number: "))        #get number in range
        user_input_numbers.append(numbers)

    average = sum(user_input_numbers) / len(user_input_numbers) #average

    print(f"first number is {user_input_numbers[0]}")               #first number
    print(f"The last number is {user_input_numbers[-1]}")           #last number
    print(f"The smallest number is {min(user_input_numbers)}")      #min number
    print(f"The largest number is {max(user_input_numbers)}")       #max number
    print(f"The average of the numbers is {average}")               #average number


main()
