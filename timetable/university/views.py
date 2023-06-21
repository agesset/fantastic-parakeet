from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(render, 'university/index.html')