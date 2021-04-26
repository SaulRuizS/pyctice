inputNumber = input("Enter some numbers: ")

numbersDictionary = {
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}

for character in inputNumber:
    print(numbersDictionary[character])     #Not really much to comment