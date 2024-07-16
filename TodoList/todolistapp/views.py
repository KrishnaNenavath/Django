from django.shortcuts import render, redirect
from .models import Todolist
from .froms import TodoListForms
from django.views.decorators.http import require_POST


# Create your views here.

def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodoListForms()
    context = {"todo_items": todo_items, 'form': form}
    return render(request, 'todolistapp/index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForms(request.POST)
    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.comlited = True
    todo.save()

    return redirect('index')

def deletecompleted(request):
    Todolist.objects.filter(comlited=True).delete()
    return redirect('index')

def deleteall(request):
    Todolist.objects.all().delete()
    return redirect('index')