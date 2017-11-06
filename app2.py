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

    # a list of similar words in the case of a typo
    close_matches = get_close_matches(word, data.keys())

    # we need to allow for proper nouns (actually capitalized in the dictionary)
    # do we're building this list of proper nouns to check again before we lowercase input like "Paris"
    proper_nouns = [entry for entry in data.keys() if entry[0].isupper()]

    # most keys are lowercase
    # so we normalize input here unless it's a proper noun
    word = word if word in proper_nouns else word.lower()

    # best case scenario
    if word in data:
        print("Ok. Here's what I found for '{}': ".format(word))
        return data[word]

    # if close_matches has a value, we may have a typo
    # track where we're at with trying to find a match
    # offer the most likely alternative and go from there
    elif close_matches:

        y_or_n = input("Can't find '{}'' Did you mean '{}'' instead? Y/N?  ".format(word, close_matches[0])).lower()
        if y_or_n == "y":
            print("okay. here's the definition for {}: ".format(close_matches[0]))
            return data[close_matches[0]]

        # this means we've tried the closest match and it wasn't right
        # we're offering the next best close_match
        elif y_or_n == "n":

            second_try = input("Was it '{}'? Y/N >>  ".format(close_matches[1])).lower()

            # if we finally got it, we'll display results
            if second_try == "y":
                print("Okay. Here's my definition of '{}'".format(close_matches[1]))
                return close_matches[1]

            # otherwise, we'll just try again
            else:
                new_word = input("Okay. Let's try this again. Please re-enter the word:  ")
                new_try = translate(new_word)
                return new_try

        else:
            return "Hmmm...I don't understand."
    else:
        return "We don't have that word. Please double check it."


if __name__ == '__main__':

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
