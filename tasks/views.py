from django.shortcuts import render, reverse, redirect
from django.views.decorators.http import require_POST

from .forms import NewTaskForm
# Create your views here.
tasks_list = ["Primer tarea", "Segunda tarea", "Tercer tarea"]

def index(request):

    return render(request, 'tasks/index.html', {"tasks_list": tasks_list})


def add(request):

    if request.POST:
        #tarea = request.POST['task']
        #tasks_list.append(tarea)

        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data['task']

            tasks_list.append(task)

            return redirect(reverse('tasks:index'))

        else:
            return render(request, 'tasks/add.html', {"form": form})

    return render(request, 'tasks/add.html', {"form": NewTaskForm})


def show_to_delete(request):

    return render(request, 'tasks/delete.html', {"tasks_list": tasks_list})
@require_POST
def delete(request):
    print(request.POST)
    task = request.POST['task']
    tasks_list.remove(task)
    return redirect(reverse('tasks:index'))
