

#memu
menu = ("(H)ello\n"
        "(G)oodbye\n"
        "(Q)uit")

#uesr name input
name = input("Enter name: ")

#get menu
print(menu)

#while loop for input
choice = input(">>> ").upper()                              #had to lookup how to make input not case sensitive (https://stackoverflow.com/questions/50192965/how-to-make-user-input-not-case-sensitive)
while choice != "Q":                                        #error correction
    #if loop for the menu choice
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    #print menu to show the menu again after each choice
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")

