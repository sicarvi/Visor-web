from django.shortcuts import render

# Create your views here.

def landing1(request):
    return render(request, "index.html")