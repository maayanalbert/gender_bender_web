from django.test import TestCase
from .pronounDictMaker import createEntries, getPlural, addPairToDict
from .nameDictMaker import getNamesInText, getNameFile, getLevenshteinDist
from .genderBender import replaceWords, seperateWords

class GenderBenderTester(TestCase):
    def testSeperateWords(self):
        string1 = "Harry, you're a wizard"
        string2 = "The policeman asked the woman"

        wordArr1 = seperateWords(string1)
        wordArr2 = seperateWords(string2)

        assert(wordArr1 == ["Harry", ",", "", " ", "you", "'", "re", " ", "a", 
                            " ", "wizard"])

        assert(wordArr2 == ["The", " ", "police", "man", " ", "asked",
                            " ", "the", " ", "", "woman"])

    def testReplaceWords(self):
        nameDict = dict()
        nameDict["Olive"] = "Oliver"
        nameDict["Mark"] = "Mary"

        pronounDict = dict()
        pronounDict["woman"] = "man"
        pronounDict["man"] = "woman"

        wordArr = ["Olive", "is", "a", "woman", ",", "Mark", "is", "a", "man"]
        bentWordArr = ["Oliver", "is", "a", "man", ",", "Mary", "is", "a", "woman"]
        replaceWords(wordArr, nameDict, pronounDict)
        print(wordArr)
        assert(wordArr == bentWordArr)

class PronounTester(TestCase):

    def testGetPlural(self):
        assert(getPlural("mr") == "mr")
        assert(getPlural("ms") == "ms")
        assert(getPlural("mistress") == "mistresses")
        assert(getPlural("s") == "ss")
        assert(getPlural("friend") == "friends")

    def testCreateEntries(self):
        d = dict() 
        word = "earl"
        oppword = "countess"
        createEntries(word, oppword, d)
        assert(d["earl"] == "countess")
        assert(d["earls"] == "countesses")
        assert(d["Earl"] == "Countess")
        assert(d["Earls"] == "Countesses")
        assert(d["EARL"] == "COUNTESS")
        assert(d["EARLS"] == "COUNTESSES")

    def testAddPairToDict(self):
        pair1 = ["earl", "countess", "o"]
        pair2 = ["duke", "duchess"]
        d = dict()
        addPairToDict(pair1, d)
        assert(d["earl"] == "countess")
        assert("countess" not in d)
        addPairToDict(pair2, d)
        assert(d["duke"] == "duchess")
        assert(d["duchess"] == "duke")

class NameTester(TestCase):
    def testGetNameFile(self):
        getNameFile(2002)
        getNameFile(1877)
        getNameFile(2200)

    def testGetLevenshteinDist(self):
        assert(getLevenshteinDist("Burr", "Sir") == 3)
        assert(getLevenshteinDist("Alexander", "Alexander") == 0)
        assert(getLevenshteinDist("Sara", "Sarah") == 1)

    def testGetNamesInText(self):
        maleNames = dict()
        A = dict()
        A["Alexander"] = 51
        maleNames["A"] = A

        femaleNames = dict()
        E = dict()
        E["Eliza"] = 20
        E["Elizabeth"] = 10
        femaleNames["E"] = E

        wordArr = ["Alexander", " ", ";", "loves", "Eliza"]
        names = getNamesInText(wordArr, maleNames, femaleNames)
        assert("Eliza" not in names)
        assert(names["Alexander"] == "M")
        assert("Elizabeth" not in names)
