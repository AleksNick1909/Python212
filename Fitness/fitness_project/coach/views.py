from django.shortcuts import render
from .models import Coach  # получаем доступ к данным в бд
from django.contrib.auth.forms import UserCreationForm

def index(request):
    projects = Coach.objects.all()  # достаем все данные и записываем в переменную
    return render(request, 'skills/index.html', {'projects': projects})


def signupuser(request):
    return render(request, 'skills/signupuser.html', {'form': UserCreationForm()})
