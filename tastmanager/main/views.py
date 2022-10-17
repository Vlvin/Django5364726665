from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': '[Вставить название]', 'tasks': tasks})



def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == "GET":
        form = TaskForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма некорректна'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
