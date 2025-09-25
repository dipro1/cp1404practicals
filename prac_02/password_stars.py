
MINIMUM_LENGTH = 10                                                             #set initial password requirements

password = input("Please enter your password: ")                                #get user password

while len(password) < MINIMUM_LENGTH:                                           #error correction
    print(f"Password needs to be at least {MINIMUM_LENGTH} character long")

    password = input("Please enter your password: ")                            #get correct password


print("*"*len(password))                                                        #print hidden password
