import string

from .pronounDictMaker import getPronounDict
from .nameDictMaker import getNameDict

defaultInputPath = "../original_texts/"
defaultOutputPath = "../bent_texts/"

# genderbends the text
# INPUT: original string of contents, the year it was written
# OUTPUT: a string of genderbent contents
def bend(rawContents, year = 2018):
    
    # get the contents in a parseable form
    wordArr = seperateWords(rawContents)

    # get the dictionaries
    print("Getting pronoun dictionary...")
    pronounDict = getPronounDict()
    print("Getting name dictionary...")
    nameDict = getNameDict(wordArr, year)
    print("Replacing words...")

    # replace the words
    replaceWords(wordArr, nameDict, pronounDict)

    # return the contents in its original format
    return "".join(wordArr)

# parses the raw contents
# INPUT: raw contents
# OUTPUT: an array of words
def seperateWords(rawContents):
    wordArr = [""]
    letters = set(string.ascii_letters)

    # iterate thrugh every character in the text
    for i in range(len(rawContents)):
        char = rawContents[i]
        
        # isolate man and woman when it appears at the end of a word
        manLen = len("man")
        womanLen = len("woman")

        if(i <= len(rawContents)-manLen and 
            (len(wordArr[-1]) == 0 or len(wordArr[-1]) > 3) and
            (rawContents[i:i+manLen] == "man" or rawContents[i:i+manLen] == "men")):
                wordArr.append(char)

        elif(i <= len(rawContents)-womanLen and 
            (rawContents[i:i+womanLen] == "woman" or rawContents[i:i+womanLen] == "women")):
                wordArr.append(char)

        # if it's a letter add it to the most recent word
        elif(char in letters):
            wordArr[-1] += char
        
        # if it isn't append it as an individual item 
        else:
            wordArr.append(char)
            wordArr.append("")

    return wordArr

# replaces every male word with a female one and vice versa
# INPUT: original word array, dictionary of names and pronouns
# OUTPUT: genderbent word array
def replaceWords(wordArr, nameDict, pronounDict):
    # iterate through every word 
    for i in range(len(wordArr)):
        word = wordArr[i]

        # if its a gendered pronoun or name switch it
        if(word in pronounDict):
            wordArr[i] = pronounDict[word]
        if(word in nameDict):
            wordArr[i] = nameDict[word]
