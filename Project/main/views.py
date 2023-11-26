from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by("-id")

    info = {
        "title": "Главная страница",
        "tasks": tasks
    }

    return render(request, "main/index.html", info)

def about(request):

    info = {
        "title": "Об нас"
    }

    return render(request, "main/about.html", info)

def createtask(request):
    error = ""

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect("home")
        else:
            error = "Форма была не вырной"

    form = TaskForm()

    info = {
        "title": "Создание задачи",
        'form': form,
        'Error': error
    }

    return render(request, "main/createtask.html", info)