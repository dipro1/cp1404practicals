def main():
    user_input_numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    user_name = input("please enter your username: ")

    if user_name in usernames:
        print("Access granted")
    else:
        print("Access denied")

    for i in range(5):
        numbers = int(input("number: "))
        user_input_numbers.append(numbers)

    average = sum(user_input_numbers) / len(user_input_numbers)

    print(f"first number is {user_input_numbers[0]}")
    print(f"The last number is {user_input_numbers[-1]}")
    print(f"The smallest number is {min(user_input_numbers)}")
    print(f"The largest number is {max(user_input_numbers)}")
    print(f"The average of the numbers is {average}")


main()
