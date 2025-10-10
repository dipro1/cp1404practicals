import random

# Constants
NUMBERS_PER_PICK = 6
MIN = 1
MAX = 45


def main():
    try:
        number_of_picks = int(input("How many quick picks? "))
    except ValueError:  # error check
        print("Invalid input please enter a number")  # error message
        return

    for i in range(number_of_picks):
        quick_picks = generate_quick_picks()
        quick_picks.sort()  # Sort in ascending order
        print(" ".join(f"{number:2}" for number in quick_picks))  # print with spacing


def generate_quick_picks():
    pick = []  # store picks
    while len(pick) < NUMBERS_PER_PICK:  # check for length of pick vector
        random_number = random.randint(MIN, MAX)  # get random numbers within range
        if random_number not in pick:
            pick.append(random_number)  # append
    return pick


if __name__ == "__main__":
    main()
