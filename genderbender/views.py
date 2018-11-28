from django.shortcuts import render
from django.http import HttpResponse
from .genderBender import bend

# Create your views here.
def default(request):
    return render(request, 'genderbender/index.html',{})


def returnIntOrNone(string):
    try:
        string= int(string)
        return string
    except ValueError:
        return None

def bendInput(request):
    string = request.POST.get('string')
    year = returnIntOrNone(request.POST.get('year'))
    if(year == None):
        bentString = bend(string)
    else:
        bentString = bend(string, year)
    context = dict()

    context["bentString"] = bentString
    if(year != None):
        context["year"] = year
    return render(request, 'genderbender/index.html',context)

