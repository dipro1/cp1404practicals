import random

# Constants
NUMBERS_PER_PICK = 6
MIN = 1
MAX = 45


def main():
    number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        quick_picks = generate_quick_picks()
        quick_picks.sort()  # Sort in ascending order
        print(" ".join(f"{number:2}" for number in quick_picks))


def generate_quick_picks():
    pick = []
    while len(pick) < NUMBERS_PER_PICK:
        random_number = random.randint(MIN, MAX)
        if random_number not in pick:
            pick.append(random_number)
    return pick


if __name__ == "__main__":
    main()
