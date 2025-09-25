for i in range(1, 21, 2):
    print(i, end=' ')
print()


#a.

for i in range(0,101,10):                               #same as the first
    print(i, end=' ')
print()


#b.

for i in range(20,0,-1):                                #almost same as before
    print(i, end=' ')
print()

#c.

number_of_stars = int(input("Please give a number any number:"))

for i in range(number_of_stars):
    print("*",end=' ')
print()


#d.

#dosent actually need this line because we can use the previous input but it looks a bit nicer for the user
number_of_stars = int(input("Please give a number any number:"))


for i in range(1,number_of_stars + 1):
    print("*" * i)
print()

