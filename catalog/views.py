from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person


def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})
    # return HttpResponse("Вывод из catalo


def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get('name')
        klient.age = request.POST.get('age')
        klient.save()
    return HttpResponseRedirect('/')

