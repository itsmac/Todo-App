from django.shortcuts import render,redirect
from .models import Notes
from .forms import NotesForm

# Create your views here.

def index(request):
    items = Notes.objects.all()
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
    form = NotesForm()
    page = {
        "form" : form ,
        "items": items
    }
    return render(request,"todo/index.html",context = page)


def remove(request,id):
    item = Notes.objects.get(id = id)
    item.delete()
    return redirect('/todo/')

def edit(request,id):
    item = Notes.objects.get(id = id)
    form = NotesForm(instance=item)
    if request.method == "POST":
        form = NotesForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
    page = {
        "form" : form
    }

    return render(request,"todo/update.html",context=page)
    
