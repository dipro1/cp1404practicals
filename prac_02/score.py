"""
CP1404/CP5632 - Practical
Program to determine score status
"""




def score_status(score):                                        #function for determining score status from user input
    if score < 0 or score > 100:                                #if elif statements for the determination
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():                                                     #main function

    score = float(input("Enter score: "))                       #user input
    print(score_status(score))                                  #print the results fron score_status


if __name__ == '__main__':
    main()                                                      #call main