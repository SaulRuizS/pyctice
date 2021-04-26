numbers = [65, 656, 78, 2515, 2515, 6568, 78]

for num in numbers:
    numQuantity = numbers.count(num)                        #Count the quantity of number "num" in the actual iteration
    if numQuantity > 1:                                     #Check if there is any number repeated
        numbers.remove(num)                                 #In case there is any number repeated, it will be removed
        print("The repeated number", num, "was removed")
if numQuantity == 1:                                        #If there is not numbers repeated, then print the message
    print("There is not any number repeated")
    print(numbers)

###  BETTER VERSION

uniques = []

for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)