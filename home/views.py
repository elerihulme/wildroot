from django.shortcuts import render
from django.http import Http404

def index(request):
    return render(request, 'home/index.html')

def trigger_404(request):
    raise Http404("Testing custom 404 page")