


def get_valid_score():                                                          #get input from user

    score = float(input("please input your score: "))                       #user input
    if score < 0 or score > 100:                                #if else to get valid input
        print("Please input a valid score between 0 and 100.")
        return None
    else:
        return score



def score_status(score):                                                #score status

    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):                                                  #print the stars
    print('*' * int(score))


def main():                                                             #main

    choice = ""                                                         #initial choice
    MENU = """Menu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


    while choice != "Q":                                                #choice for quit
        print(MENU)                                                     #call menu
        choice = input(">>> ").upper()                                  #set no case sensitivity

        if choice == "G":                                               #choices
            score = get_valid_score()
        elif choice == "P":
            result = score_status(score)
            print(f"A score of {score} will be {result}")
        elif choice == "S":
            print(f"Score: {score}")
            show_stars(score)
        elif choice == "Q":
            print("Alright, test's over. \033[1m*coughing*\033[0m. You can head on back to your desk.") #exit message with flare
        else:
            print("Please input a option from the menu")


if __name__ == "__main__":
    main()
