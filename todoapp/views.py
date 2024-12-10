from django.shortcuts import render
from .models import Person
from django.http import HttpResponseNotFound, HttpResponseRedirect

def home(request):
    user = Person.objects.all()
    return render(request, 'index.html',{'user':user})


#Малымат тузуу
def create(request):
    if request.method == 'POST':
        users = Person()
        users.id = request.POST.get('id')
        users.name = request.POST.get('name')
        users.age = request.POST.get('age')
        users.save()
    return HttpResponseRedirect('/')

#Маалымат озгортуу
def edit(request,id):
    try:
        user = Person.objects.get(id=id)
        if request.method == 'POST':
            user.name = request.POST.get('name')
            user.age = request.POST.get('age')
            user.save()
            return HttpResponseRedirect('/')
        else:
            return render(request,'edit.html',{'user':user})

    except Person.DoesNotExist:
        return HttpResponseNotFound('<h1>Колдонучуу табылган жок</h1>')

def delete(request,id):
    try:
        user=Person.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h1>Колдонуучу табылган жок</h2>')