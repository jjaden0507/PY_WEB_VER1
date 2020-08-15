from django.shortcuts import render
from django.views.generic import ListView
from youtube.models import youtube

# Create your views here.
class youtubeLV(ListView):
    model = youtube