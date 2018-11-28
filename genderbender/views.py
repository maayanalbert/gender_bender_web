from django.shortcuts import render
from django.http import HttpResponse
from .genderBender import bendString

# Create your views here.
def default(request):
    return render(request, 'genderbender/index.html',{})

def bendInput(request):
    string = request.POST.get('string')
    print()
    return render(request, 'genderbender/index.html',{})

