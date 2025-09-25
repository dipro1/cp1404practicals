"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))              #ask the user for the number of sales

rate_1 = 0.1                                        #provided rate for sales lower than 1000
rate_2 = 0.15                                       #provided rate for sales 1000 and over

while sales >= 0 :                                  #while loop so that user can use it multiple times
    if sales < 1000:                                #simple if else
        bonus = sales * rate_1                      #simple calculation
    else:
        bonus = sales *  rate_2
    print("bonus = ",bonus)                         #print the result in the console

    sales = float(input("Enter sales: $"))          #loop back to the start



#there is no error correction on the above code
#using a wile true loop to judge if the user input is negative and print a message to get a valid number
#alternatively a boundary like :
# while sales >=0 or sales < 0:
# if sales <0
# print("error")
#else
#  if sales < 1000
#       bonus =
#   else:
#       bonus =
#       print ()

# this also contain nested if else statements within another if else statements

# this was not required by the prack so i didnt include it 


