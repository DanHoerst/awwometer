from random import choice
from Aww.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def default_display(request):
    animals = Animal.objects.all()
    left_animal = choice(animals)
    right_animal = choice(animals)
    while left_animal == right_animal:
        right_animal = choice(animals)
    context = RequestContext(request)
    return render_to_response('Aww/index.html', {"right_animal": right_animal, "left_animal": left_animal,}, context_instance=context)

def vote(request, animal_up, animal_down):
    animal_up = Animal.objects.get(id=animal_up)
    animal_down = Animal.objects.get(id=animal_down)
    animal_up.rating += 1
    animal_up.save()
    animal_down.rating -= 1
    animal_down.save()
    return HttpResponseRedirect('/')

