from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages


def index(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, 'index.html', context)

def new_show(request):
    return render(request, 'new_show.html')

def add_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new_show')
    else:
        Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release = request.POST['release'],
            desc = request.POST['desc'],
        )
        return redirect('/')


def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        "show": show,
    }
    return render(request, 'edit_show.html', context)

def edit(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(f'/edit/{show_id}')
    else:
        edit = Show.objects.get(id=show_id)
        edit.title = request.POST['title']
        edit.network = request.POST['network']
        edit.release = request.POST['release']
        edit.desc = request.POST['desc']
        edit.save()
    return redirect(f'/show/{show_id}')


def show(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        "show": show,
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
    delete = Show.objects.get(id=show_id)
    delete.delete()
    return redirect('/')