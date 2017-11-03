import json

data = json.load(open("data.json"))

def translate(word):
"""takes word from user and finds the definition in data"""
    if word in data:
        return data[word]
    else
        return "The word doesn't exist. Please double check it."
    return data[word]

print("what word would you like to look up??")
word = input(">> ")

print(translate(word))
