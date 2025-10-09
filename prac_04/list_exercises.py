def main():
    user_input_numbers = []

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
