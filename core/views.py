from django.shortcuts import render, HttpResponse

# Create your views here.
def holamundo(request):
    return HttpResponse(" BIENVENIDOS A DJANGO , HOLA MUNDO ")


def menu(request):
    return render(request, 'menu.html')