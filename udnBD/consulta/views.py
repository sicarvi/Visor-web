from django.shortcuts import render
from database import Database

# Create your views here.

def landing1(request):
    mongo = Database()
    if request.method == "POST" and request.POST.get("tabla"): 
        tabla = request.POST.get("tabla")
        mongo.set_table(tabla)
        todos = mongo.see_all()
        return render(request, "index.html", {"contenido":todos})

    return render(request, "index.html", {"contenido":[]})
