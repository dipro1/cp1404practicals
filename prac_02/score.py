"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


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


    random_score = random.randint(0,100)                 #generate random number inbetween 0 and 100
    print(f"A score of {random_score} will be {score_status(random_score)}")    #print the random number and the status

if __name__ == '__main__':
    main()                                                      #call main