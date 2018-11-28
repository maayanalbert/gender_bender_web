from django.shortcuts import render
from django.http import HttpResponse
from .genderBender import bend
import os


# get the text to put in the input box when it's empty
# INPUT: whether or not the person has hit genderbend yet
# OUTPUT: a welcome message if they haven't and a prompt if they have 
def getDefaultText(starting):
    if(starting == True):
        line1 = "Hello and welcome to Gender Bender!" + "\n\n"
        line2 = "To get started, type some text in here or click on one of"
        line3 = " the links to the right. Optionally, input the year the text"
        line4 = " was written in to get historically accurate names. Then, click"
        line5 = " the button below to start genderbending!"
        return line1 + line2 + line3 + line4 + line5
    else:
        return "Write some text here..."

# flip the accent color every time the user hits genderbend
# INPUT: the current color or none
# OUTPUT: the opposite color
def flipAccentColor(curColor):
    blue = "017AFE"
    pink = "FC4664"
    if(curColor == None or curColor == blue):
        return pink
    else:
        return blue

# serve the default view
# INPUT: 
# OUTPUT: the welcome message
def default(request):
    context = dict()
    context["defaultText"] = getDefaultText(True)
    context["curColor"] = flipAccentColor(None)
    return render(request, 'genderbender/index.html',context)

# check if a string can be converted to an int
# INPUT: the string in question
# OUTPUT: the integer version of the string or a nonetype 
def returnIntOrNone(string):
    try:
        string= int(string)
        return string
    except ValueError:
        return None

# genderbends the input
# INPUT: the string to be converted and optionally the year it was written in
# OUTPUT: the the converted text 
def bendInput(request):

    # get the string, year, and current color
    string = request.POST.get('string')
    year = returnIntOrNone(request.POST.get('year'))
    curColor = request.POST.get('curColor')

    # bend the text (with the year if its valid)
    if(year == None):
        bentString = bend(string)
    else:
        bentString = bend(string, year)
    context = dict()

    # populate the response data
    context["bentString"] = bentString
    context["defaultText"] = getDefaultText(False)
    context["curColor"] = flipAccentColor(curColor)
    print(curColor)
    if(year != None):
        context["year"] = year

    return render(request, 'genderbender/index.html',context)

# inserts the contents of a novel into the text inpu box
# INPUT: the name of the text file of the novel and the year it was written
# OUTPUT: the contents of the novel and the year it was written
def getNovel(request):

    # get the novel name, year it was written, and current color
    novel = request.POST.get('novel')
    novelYear = request.POST.get('novelYear')
    curColor = request.POST.get("curColor")

    
    # get the filepath of the novel
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, "novels/" + novel + ".txt")
    
    # populate the response data
    context = dict()
    context["bentString"] = open(file_path, "r").read()
    context["year"] = novelYear
    context["defaultText"] = getDefaultText(False)
    context["curColor"] = curColor
    return render(request, 'genderbender/index.html',context)

