from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Line
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def home(request):
    return render_to_response('home.html', {'lines': Line.objects.all()})
