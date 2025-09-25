


#get number of items
number_of_items = int(input("Number of items:"))

#wile loop for error
while number_of_items < 0:
    print("Please input a valid number of items")

    number_of_items = int(input("number of items:"))

#initial values
total_price = 0                                                         #total price of all items(here it is stored as a variable)
DISCOUNTS = 0.1                                                          #dicount stored as a static so that it can be used in multiple places and can be eddited later


#for loop
#price+= price
for i in range(number_of_items):
    price = float(input("price of item: "))                             #ask the user for the price of tiems
    total_price += price                                                #update the price variable
#if loop
#total = total - (total * discount)
if total_price > 100:                                                   #check if discount need to be apllied before the total price is printed
    total_price = total_price - (total_price * DISCOUNTS)                #update price variable

print(f"total price of {number_of_items} item is $ {total_price:.2f}")  #print
