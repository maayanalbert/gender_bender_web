from django.shortcuts import render
from django.http import HttpResponse
from .genderBender import bend
import os

# default view
def default(request):
    return render(request, 'genderbender/index.html',{})

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

    # get the string and year
    string = request.POST.get('string')
    year = returnIntOrNone(request.POST.get('year'))

    # bend the text (with the year if its valid)
    if(year == None):
        bentString = bend(string)
    else:
        bentString = bend(string, year)
    context = dict()

    # populate the response data
    context["bentString"] = bentString
    if(year != None):
        context["year"] = year

    return render(request, 'genderbender/index.html',context)

def getNovel(request):
    novel = request.POST.get('novel')
    novelYear = request.POST.get('novelYear')
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, "novels/" + novel + ".txt")
    context = dict()
    context["bentString"] = open(file_path, "r").read()
    context["year"] = novelYear
    return render(request, 'genderbender/index.html',context)

