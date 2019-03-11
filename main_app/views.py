from django.shortcuts import render
from django.http import HttpResponse
from .models import God
# Create your views here.
# class God:
#     def __init__(self, name, origin, description, use_for):
#         self.name = name 
#         self.origin = origin
#         self.description = description
#         self.use_for = use_for

# gods = [
#     God('kali', 'hindu', "will rip your ego's head off", 'removing anger'),
#     God('isis', 'egyptian', 'goddess of the dead', 'mourning'),
#     God('lakshmi', 'hindu', 'brings wealth and good luck', 'manifesting prosperity'),
#     God('madame pele', 'hawaiian', 'creator and destroyer', 'connecting to earth'),
#     God('artemis', 'greek', 'goddess of wilderness + the hunt', 'fertility'),

# ]

# Define the home view
def home(request):
  return HttpResponse('<h1>goddesses</h1>')

def about(request):
  return render(request, 'about.html')

def gods_index(request):
    gods = God.objects.all()
    return render(request, 'gods/index.html', { 'gods': gods })

def gods_detail(request, god_id):
    god = God.objects.get(id=god_id)
    return render(request, 'gods/detail.html', { 'god': god })