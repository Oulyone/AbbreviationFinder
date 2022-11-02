from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Abbreviation
# Create your views here.

global res, findAbbreviation

res = ''
findAbbreviation = Abbreviation ('id', 'abbreviation', 'definition', 'information')

def index(request):
    global res, findAbbreviation
    myAbbreviation = Abbreviation.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myabbreviation': myAbbreviation,
        'response' : res,
        'findAbbreviation' : findAbbreviation,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
    global res
    x = request.POST['abbreviation']
    y = request.POST['definition']
    z = request.POST['information']
    abbre = Abbreviation(abbreviation=x, definition=y, information=z)
    abbre.save()
    find(request,abbre)
    res = 'Added'
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    global res, findAbbreviation
    try:
        abbre = Abbreviation.objects.get(id=id)
    except:
        return HttpResponseRedirect(reverse('index'))
    abbre.delete()
    res = 'Deleted'
    findAbbreviation = Abbreviation ('id', 'abbreviation', 'definition', 'information')
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    try:
        abbre = Abbreviation.objects.get(id=id)
    except:
        return HttpResponseRedirect(reverse('index'))
    template = loader.get_template('update.html')
    context = {
        'myabbre': abbre,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    global res
    abbreviation = request.POST['abbreviation']
    definition = request.POST['definition']
    information = request.POST['information']
    abbre = Abbreviation.objects.get(id=id)
    abbre.abbreviation = abbreviation
    abbre.definition = definition
    abbre.information = information
    abbre.save()
    find(request,abbre)
    res = 'Updated'
    return HttpResponseRedirect(reverse('index'))

def find(request,abbre=''):
    global res, findAbbreviation
    try:
        abbreviation = request.POST['abbreviation']
    except:
        abbreviation = abbre.abbreviation
    try:
        findAbbreviation = Abbreviation.objects.get(abbreviation=abbreviation)
    except:
        res = 'Not found!'
        return HttpResponseRedirect(reverse('index'))
    res = 'Found!'
    findAbbreviation = findAbbreviation
    return HttpResponseRedirect(reverse('index'))