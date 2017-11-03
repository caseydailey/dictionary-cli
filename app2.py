import json
from difflib import get_close_matches

"""
get_close_matches(word, possibilities, n=3, cutoff=0.6)
    Use SequenceMatcher to return list of the best "good enough" matches.

    word is a sequence for which close matches are desired (typically a
    string).

    possibilities is a list of sequences against which to match word
    (typically a list of strings).
"""

# type(data) = dictionary
data = json.load(open("data.json"))

def translate(word):
    """takes word from user and finds the definition in data"""

    # data is all in lowercase
    # so we normalize input here
    word = word.lower()

    # a list of similar words in the case of a typo
    close_matches = get_close_matches(word, data.keys())

    if word in data:
        print("Ok. Here's what I found for '{}': ".format(word))
        return data[word]
    elif len(close_matches) > 0:
        y_or_n = input("Can't find '{}'' Did you mean '{}'' instead? Y/N?  ".format(word, close_matches[0])).lower()
        if y_or_n == "y":
            print("okay. here's the definition for {}: ".format(close_matches[0]))
            return data[close_matches[0]]
        elif y_or_n == "n":
            return "Sorry. I can't find that word."
        else:
            return "Hmmm...I don't understand."
    else:
        return "The word doesn't exist. Please double check it."


print("welcome to the cli dictionary. what word would you like to look up?")
word = input(">> ")

output = translate(word)

if type(output) == list:
    for i, item in enumerate(output):
        if len(output) > 1:
            print("{}. {}".format((i + 1), item))
        else:
            print(item)
else:
    print(output)
