from django.shortcuts import render
from database import Database

# Create your views here.

def landing1(request):
    mongo = Database("BD_profesores")
    todos = mongo.see_all()
    #TODO crear un switch para determinar la coleccion a cargar, y asi determinar de una lista posible de vars el nombre y apellido
    #para el front
    return render(request, "index.html", {"contenido":todos})
