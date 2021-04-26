message = input("Write a message with an emoticon: ")
words = message.split(" ")

emojis = {
    ":)":"😊",
    ":(":"😢",
    ">:(":"😠",
    "XD":"🤣",
    ":D":"😀",
    ":/":"😕",
    ":p":"😛"
}

phrase = ""
for word in words:
    phrase += emojis.get(word, word) + " "
print(phrase)

#Not really much to comment